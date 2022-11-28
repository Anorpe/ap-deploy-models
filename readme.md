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
