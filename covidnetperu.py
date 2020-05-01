import numpy as np
import cv2
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras import backend as K
from config import conf_rutas as rutas

class CovidNetPeru:
    def __init__(self):
        self.frxt_longitud, self.frxt_altura = 64, 64
        self.frxt_modelo = rutas.frxt_directorio + rutas.frxt_archivo_modelo
        self.frxt_pesos = rutas.frxt_directorio + rutas.frxt_archivo_pesos
        self.frxt_invmap = {0: 'otro', 1: 'torax'}
        self.graph_filtro = tf.Graph()
        with self.graph_filtro.as_default() as g0:
            self.sess_filtro = tf.Session(graph=g0)
            set_session(self.sess_filtro)
            self.frxt = tf.keras.models.load_model(self.frxt_modelo)
            self.frxt.load_weights(self.frxt_pesos)

        self.cnet_metaname = rutas.cnet_directorio + rutas.cnet_metaname
        self.cnet_ckptname = rutas.cnet_directorio + rutas.cnet_ckptname
        self.cnet_map = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
        self.cnet_invmap = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}
        self.graph_cnet = tf.Graph()
        with self.graph_cnet.as_default() as g1:
            self.sess_cnet = tf.Session(graph=g1)
            saver = tf.train.import_meta_graph(self.cnet_metaname)
            saver.restore(self.sess_cnet, self.cnet_ckptname)
        self.cnet_image_tensor = self.graph_cnet.get_tensor_by_name("input_1:0")
        self.cnet_pred_tensor = self.graph_cnet.get_tensor_by_name("dense_3/Softmax:0")

    def predict(self, path_file):
        result_filtro = None
        x_filtro = load_img(path_file, target_size=(self.frxt_longitud, self.frxt_altura))
        x_filtro = img_to_array(x_filtro)
        x_filtro = np.expand_dims(x_filtro, axis=0)
        with self.graph_filtro.as_default():
            set_session(self.sess_filtro)
            array = self.frxt.predict(x_filtro)
            result = array[0]
            answer = np.argmax(result)
            result_filtro = answer
            if answer == 1:# corresponde a torax
                pass
                #print(path_file, 'es imagen de', self.frxt_invmap[answer])

        if result_filtro and result_filtro == 1:
            x_cnet = cv2.imread(path_file)
            x_cnet = cv2.resize(x_cnet, (224, 224))
            x_cnet = x_cnet.astype('float32') / 255.0
            pred = self.sess_cnet.run(self.cnet_pred_tensor, feed_dict={self.cnet_image_tensor: np.expand_dims(x_cnet, axis=0)})
            result_cnet = pred.argmax(axis=1)[0]
            #print('Resultado predicción: {}'.format(self.cnet_invmap[result_cnet]))
            return {'result': self.cnet_invmap[result_cnet], 'message': 'imagen clasificada'}
        else:
            return {'result': 'null','message': 'imagen desconocida'}