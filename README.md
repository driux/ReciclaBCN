# BCleaN

## Inspiración
¿Por qué la gente no recicla? Hemos llegado a la conclusión de que se debe a que la gente no cuenta con la información necesaria como dónde estan los puntos verdes, cuándo pasan a recoger la basura o a qué contenedor va. Por eso, hemos hecho una webapp para facilitar el reciclaje diario.

## ¿Qué hace?
Es una app que cuenta con diferentes partes:
* Dada una imagen por el usuario te dice a qué contenedor va.
* Si no lo detecta correctamente, te pregunta si es organico y si no te da un enlace al punto verde más cercano.
* Permite reportar si un contenedor está lleno o en mal estado. 
* Contiene un sistema de puntos que premia el reciclaje y la colaboración.
* Aporta curiosidades sobre el medio ambiente para concienciar.

## Cómo lo construimos
Nos dividimos el trabajo en 3 partes:
1. **Diseño de interfaz:** Se han escogido colores para representar al medio ambiente. Para los contenedores se buscaron iconos minimalistas para hacer más intuitiva la aplicación. También se ha tenido en cuenta que será ejecutada en móvil.
2. **Detector de imágenes para la basura:** Utilizando la librería fastai de python se ha entrenado una CNN de 34 capas con unas 2000 imágenes de una base de datos online con imágenes de basura clasificada.
3. **Base de datos:** Todo ha sido creado usando python para ejecutar los script de SQL. Primero crea las tablas y una vez creadas se han ido rellenando con información online en el caso de los puntos verdes y de forma manual las que serían usadas como ejemplo.

## Problemas que nos hemos encontrado
El principal inconveniente es que hemos tenido que aprender todo desde cero. Por otro lado, nos costó bastante tiempo encontrar las bases de datos de imágenes y la de puntos verdes, que de hecho estaba en un formato poco manejable. Además, con la capacidad de procesamiento que teníamos ha resultado difícil entrenar de forma aceptable la CNN.

## Logros de los que nos sentimos orgullosos
Principalmente de haberlo conseguido. Hemos conseguido plasmar la idea inicial al detalle. Junto con todo lo que hemos aprendido en el proceso.

## ¿Qué hemos aprendido?
A manejar correctamente un repositorio de github entre varias personas. También, hemos aprendido a usar flask para hacer servidores en python. Y a utilizar la librería fastai para clasificar imágenes. Además, ahora sabemos crear bases de datos desde python y cambiar el formato de un dataset de xml a json.

## ¿Qué será lo siguiente para BCleaN?
Crear un sistema de usuarios real que respete la privacidad de la gente. Añadir un apartado que avise de cuándo pasan a recoger un mueble. Mejorar el modelo de detección de imágenes para detectar orgánico además de plástico, latas, papel y cartón. 

## Programado con
`python` `javascript` `sql` `html` `flask`

## Try it out
[Github repo](https://github.com/raulhigueras/ReciclaBCN)
