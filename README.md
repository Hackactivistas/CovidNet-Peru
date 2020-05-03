# CovidNet-Peru [![CCLicence][cc-img]][cc]
> Una propuesta de desarrollo colectivo para el diagnóstico temprano de COVID-Perú.

Se trata de una tecnología open source basado en un modelo de redes neuronales convolucionales con aprendizaje profundo para el pre-diagnóstico del COVID-19 mediante imágenes de radiografía del Tórax


[cc-img]:      https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png
[cc]:          https://creativecommons.org/licenses/by-nc-sa/4.0/


## Presentación
En tiempos tan críticos como la actual pandemia necesitamos de una gobernanza abierta que promueva el desarrollo tecnológico del software libre, herramientas eficientes y confiables de acceso abierto a la innovación continua. Nos encontramos en plena crisis sanitaria y transformación digital (la llamada 4ta Revolución Industrial), por ello es que nace COVIDNetPerú, una propuesta open source que complementa al diagnóstico del COVID-19 utilizando radiografías de tórax mediante la inteligencia artificial.

Nuestro software es una iniciativa de ciencia ciudadana, la cual motiva a la integración cultural basado en un modelo de autogestión colaborativa entre científicos activistas independientes (o Hackactivistas). 

La reestructuración de nuevas organizaciones societarias emerge en cada crisis socio-económica, en este contexto, nuestras sociedades latinoamericanas tienen la oportunidad de liderar la innovación social digital impulsando una economía orientada a los bienes comunes desde una política de libre cooperación entre redes autónomas.

## Descripción del proyecto
El COVID-19 está dejando en el Perú un triple impacto a nivel sanitario, económico y educativo, siendo el segundo país en Latinoamérica con el mayor número de infectados confirmados con más de 30 mil casos (y una aparente tasa de letalidad del 2.8%). Arrastramos una deficiencia en nuestro sistema de salud que retrasa la respuesta terapéutica, tal como lo refiere Soto A (2019) (1), revelando las barreras para una atención eficaz en los hospitales de referencia del Ministerio de Salud, la falta de equipos tecnológicos modernos para el diagnóstico temprano y tratamiento oportuno. 

Siendo ese el principal desafío para las enfermedades emergentes infecto-contagiosas, como el COVID-19, lograr una implementación de efectivos métodos diagnósticos que aceleren la detección de los casos infectados. Siendo la prueba molecular PCR (el gold standard) para COVID-19, pese a que tiene una sensibilidad variable entre el 37-71% (2). Estás vienen siendo reforzadas por las pruebas “rápidas” de tipo serológicas que, partir de la segunda semana de iniciada la enfermedad, presentan apenas un 33% de sensibilidad (3). 

Es así que planteamos una adaptación del protocolo de atención a persona con sospecha de COVID-19 sugerido por la OMS (4), como medida post-cuarentena, así agilizar la identificación y el monitoreo de nuevos casos de contagio (Figura 1). Tal como se hizo en Codogno (Italia) durante la etapa post-cuarentena, implementando una rápida medida de screening en zonas de alto riesgo de transmisión comunitaria, tras intervenir a asintomáticos o mínimamente sintomáticos usando radiografías de tórax como método pre-diagnóstico (4). Adicionalmente, potenciar dicho método diagnóstico mediante el autómata inteligente integrado a un agente conversacional (o chatbot) que permita orientar al ciudadano durante el proceso de triaje. 

<img src="/imagenes/Protocolo de asistencia rápida para descarte COVID19.png" align="center" />

Nuestra propuesta COVIDNet-Perú se presenta como una alternativa de bajo costo, fácil acceso y alta confiabilidad, basado en el diseño inteligente que incluso permitiría la reducción del burnout en el personal médico. Este modelo consiste en una red neuronal convolucional profunda basada en una arquitectura diseñada bajo la visión de colaboración humano-maquina inspirada en el estudio de Wang L. and Wong A. (2020).

## Resultados previos

Hemos generado una validación previa del modelo de inteligencia artificial, basado en el desarrollo de un estudio previo (7), utilizando 1635 imágenes radiográficas clasificadas como i) rx normal, ii) rx neumonía y iii) rx COVID. En tal sentido, logramos pre-entrenar nuestro modelo con dicha dataset, además, hemos dotado a nuestro modelo nuevos filtros de discriminación que permite identificar solo radiografías de tórax entre cualquier otro tipo de imagen. 

<img src="/imagenes/Web.jpg" align="center" />

En total nuestro modelo presenta tres procesos (o capas) de identificación: una primera capa de discriminación de imágenes radiográficas, una segunda capa de detección de radiografías con patrones de una neumonía viral tipo COVID y, por último, una última capa que permite verificar lesiones respiratorias adicionales. De este modo fue diseñada la arquitectura de nuestro algoritmo COVIDNet-Perú, adicionalmente hemos programado un chatbot en Fb messenger ponderando las respuestas en base a los criterios clínicos-epidemiológicos para un correcto triaje. 

<img src="/imagenes/Flujograma COVIDNet-Peru.png" align="center" />

## Propuesta de desarrollo colectivo

Para llevar a cabo el desarrollo de este software inteligente nos basaremos en tre hitos, los mismos que responden a nuestros tres objetivos específicos:

- Validación del modelo de inteligencia artificial mediante las redes neuronales convolucionales utilizando imágenes radiográficas de tórax. 
- Implementación de un agente conversacional (chatbot) de orientación ciudadana para el triaje clínico-epidemiológico.
- Desarrollo del sistema integrado para la automatización diagnóstica de COVID-19 en el servicio de radiología.

La base para lograr un sistema integral inteligente (https://github.com/minskylab/asclepius), se fundamenta en la modularidad, la escalabilidad, la distribución y el data-driven. Siguiendo esos lineamientos la visión detrás de nuestro software inteligente podremos alcanzar la transformación tecnológica a gran escala para completar la brecha digital que tiene el sistema de salud en el país. 

	
<img src="/imagenes/Propuesta de Desarrollo Colectivo.png" align="center" />


## Referencias:

https://github.com/lindawangg/COVID-Net

https://github.com/aildnont/covid-cxr

https://medium.com/sheldon.fernandez/covid-net-larger-dataset-new-models-and-covid-risknet-fd8e7c451c



Contactos:

ialabs@hackactivistas.org, edwincc@tenzorgroup.com, jhosepvega2015@gmail.com, david.chaupis.m@upch.pe, samuel.electronica@gmail.com, edronald7@gmail.com
