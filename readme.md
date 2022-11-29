# Despliegue de un modelo de Machine Learning como una API REST

Este repositorio tiene un ejemplo de despliegue de un modelo de clasificación del conjuntos de datos "iris dataset" como una API REST utilizando FastAPI mediante un contenedor docker;
El contenido del repositorio es el siguiente:

- models : Carpeta con los modelos guardados.
- Dockerfile : Archivo para la creación de la imagen docker.
- main.py : Script python de la API.
- model development.ipynb : Notebook del desarrollo del modelo.
- requirements.txt : Archivo con las dependencias necesarias.

# Instrucciones de despliegue en Heroku

-	Descargar e instalar docker desktop https://www.docker.com/ 
-	Descargar e instalar Visual Studio Code https://code.visualstudio.com/ .
-	Descargar e Instalar extensión de Docker para Visual Studio. 
-	Descargar e Instalar Postman https://www.postman.com/. 
-	Descargar e instalar Heroku CLI https://devcenter.heroku.com/articles/heroku-cli . 
-	Abrir una terminal en el directorio donde están los archivos de la API y el Dockerfile y escribir los siguientes comandos: 

    - heroku login
    - docker ps
    - heroku container:login
    - heroku container:push web –app %appNameHeroku%
    - heroku container:release web –app %appNameHeroku%
