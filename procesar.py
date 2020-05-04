import pandas as pd
from os import listdir
from os.path import isfile, join
from covidnetperu import CovidNetPeru

class RunCovidNetPeru:
    def __init__(self):
        self.cnetperu = CovidNetPeru()

    def procesar_uno(self, ruta_archivo):
        datos = self.cnetperu.predict(ruta_archivo)
        resultado, mensaje = datos.get('result'), datos.get('message')
        if resultado!='null':
            print('El resultado de evaluación es: {}'.format(resultado))
            print('{}, {} \n'.format(mensaje, ruta_archivo))
        else:
            print('Error porque no se reconoce la imagen como Rayos X del Torax')
            print('{}, {} \n'.format(mensaje, ruta_archivo))

    def procesar_lote(self):
        carpeta_covid = 'dataset/covid19/'
        carpeta_normal = 'dataset/normal/'
        imagenes_covid = [join(carpeta_covid, f) for f in listdir(carpeta_covid) if isfile(join(carpeta_covid, f))]
        imagenes_normal = [join(carpeta_normal, f) for f in listdir(carpeta_normal) if isfile(join(carpeta_normal, f))]
        list_covid = list(zip(imagenes_covid, ['Covid19' for n in range(len(imagenes_covid))]))
        list_normal = list(zip(imagenes_normal, ['normal' for n in range(len(imagenes_normal))]))
        list_total = list_covid + list_normal
        print("Procesando {} imagenes, donde {} son covid19 y {} son normales (no-covid).".format(len(list_total),
                                                                                         len(imagenes_covid),
                                                                                         len(imagenes_normal)))
        df = pd.DataFrame(list_total, columns=['Imagen', 'Clase_Real'])
        df['Clase_Prediccion'] = ''
        df['Observaciones'] = ''
        for indice, fila in df.iterrows():
            datos = self.cnetperu.predict(fila['Imagen'])
            resultado, mensaje = datos.get('result'), datos.get('message')
            df.loc[indice, 'Clase_Prediccion'] = resultado if resultado!='null' else ''
            df.loc[indice, 'Observaciones'] = 'No se logra reconocer como imagen de Rayos X del Torax' if resultado=='null' else ''
        df.to_excel('resultado_covidnetperu.xlsx', index=False)

if __name__=='__main__':
    run_cnp = RunCovidNetPeru()

    # Pruebas una a una
    run_cnp.procesar_uno('imagenes/muestra1.png')
    run_cnp.procesar_uno('imagenes/muestra2.png')
    run_cnp.procesar_uno('imagenes/muestra3.png')
    run_cnp.procesar_uno('imagenes/muestra4.jpg')
    run_cnp.procesar_uno('imagenes/muestra5.jpeg')
    run_cnp.procesar_uno('imagenes/muestra6.jpg')

    # Pruebas masivas
    run_cnp.procesar_lote()