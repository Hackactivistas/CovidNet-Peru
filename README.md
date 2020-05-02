# CovidNet-Peru
> Una propuesta de desarrollo colectivo para el diagnóstico temprano de COVID-Perú.





Una tecnología open source de aprendizaje profundo para el pre-diagnóstico del COVID-19 mediante imágenes de radiografía del Tórax
### Problemática
En tiempos tan críticos como la actual pandemia, necesitamos de herramientas tecnológicas eficientes y confiables para ayudar a enfrentar la enfermedad en todas las etapas, en este caso esta iniciativa supone complementar en el diagnóstico rápido de la enfermedad sobre todo en la región de Latinoamericana. Perú es el segundo país de la región con mayor nivel de infectados (al 29 de abril con más de 33 mil casos confirmados), después de Brasil.
Utilizar las imágenes radiológicas (radiografías y/o tomografías) como primera medida para la detección temprana de COVID19 permitiría reconocer el real panorama de infectados a nivel comunitario. El uso de radiografías representa una herramienta accesible, de bajo costo y rápida respuesta para detectar patrones neumónicos por SARS-CoV-2.
Si bien las radiografías no presentan una alta sensibilidad en los primeros cinco días de la infección, son las tomografías una excelente opción de diagnóstico temprano a comparación de las pruebas moleculares (PCR-RT) que han presentado una sensibilidad variable entre 37% a 71%.
### Solución
En ese sentido, nuestro equipo de investigación yo, Jhosep, David y Samuel elaboramos una propuesta de un desarrollo tecnológico con base científica llamado COVIDNet-Perú. Se trata de un modelo de inteligencia artificial capaz de predecir la infección por COVID-19 mediante pruebas radiográficas. Este modelo consiste en una red neuronal convolucional profunda basada en una arquitectura diseñada a partir de la colaboración humano-maquina influenciada en el estudio de Wang L. and Wong A. (2020).
El modelo ha pasado por una prueba de entrenamiento mediante indicadores de funcionalidad (sensibilidad, especificidad y precisión) a partir de una dataset de 16756 imágenes radiográficas de tórax, clasificados en tres posibles resultados como: a) casos sanos, b) casos neumonía y, c) COVID19. Adicionalmente, permite el autómata inteligente discriminar entre una imagen radiográfica de tórax y otros tipos de imágenes que induzcan al error por ser de fuente desconocida no radiográfica.

[imagen1] 

### Resultados
Para casos peruanos (20 covid y 50 sanos), el Modelo COVIDNet-Perú pudo predecir (con una sensibilidad del 94%, especificidad del 96% y precisión del 96%) en un 96% los casos sanos (48/50; predecidos/reales) reduciendo el riesgo de falsos negativos, asimismo, en un 79% los casos confirmados de COVID-19, detectando el patrón radiográfico relacionado a neumonía atípica (11/13; predecidos/reales).

[imagenes]

#### Propuestas
Nuestra propuesta va dirigida a incentivar a un ecosistema de colaboración científica a través de centros de salud o clínicas privadas interesados en apoyar esta iniciativa de software abierto para la comunidad latinoamericana. 
Buscamos integrar esfuerzos, así que aquellos equipos de IA interesados en sumarse pueden contactarse con nosotros.

##### Referencias:
https://github.com/lindawangg/COVID-Net

https://github.com/aildnont/covid-cxr

https://medium.com/sheldon.fernandez/covid-net-larger-dataset-new-models-and-covid-risknet-fd8e7c451c



Contactos:

ialabs@hackactivistas.org, edwincc@tenzorgroup.com, jhosepvega2015@gmail.com, david.chaupis.m@upch.pe, samuel.electronica@gmail.com, edronald7@gmail.com
