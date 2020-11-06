# Explicación configuración Docker

## Paso 1: Registrarse en Docker hub
Primero hay que crearse una cuenta en [Docker hub](https://hub.docker.com/)


Una vez registrado, nos vamos a settings -> Linked Accounts & Services, pinchamos sobre github y aceptamos la autorización.

Seguidamente creamos un repositorio con el nombre de nuestro proyecto, eso sí en minuscula porque dockerhub trabaja con lowercase.

![img](https://github.com/JaviPrieto/PeluqueriaUnisex/docs/img/docker-repo.png)

## Paso 2: Instalar Docker

[Documentación Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)

Actualizamos los paquetes:

	$ sudo apt-get update

Instalamos los paquetes necesarios: 

	$ sudo apt-get install \
	    apt-transport-https \
	    ca-certificates \
	    curl \
	    software-properties-common

Añadimos la key GPG oficial de Docker:

	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verificamos la clave:

	$ sudo apt-key fingerprint 0EBFCD88

Establecemos un repositorio estable:

	$ sudo add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	   $(lsb_release -cs) \
	   stable"

Actualizamos paquetes e instalamos la última versión de Docker:

	$ sudo apt-get update
	$ sudo apt-get install docker-ce

Verificamos si se ha instalado correctamente:

	$ sudo docker run hello-world

## Paso 3: Crear Dockerfile

En el Dockerfile pondremos las ordenes que necesitamos para crear la imagen:

![img](https://github.com/JaviPrieto/PeluqueriaUnisex/docs/img/dockerfile-img.png)

## Paso 4: Desplegar en Heroku

[Documentación Heroku.yml](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

Creamos una aplicación nueva en heroku, a la que llamare contenedor-citas.

Creamos el archivo heroku.yml para que cree la imagen desde el dockerfile.

	build:
	  docker:
	    web: Dockerfile
	run:
	  web: cd src && **gunicorn** main.py

Si no funciona con **gunicorn** ponemos **python**.

Indicamos en Heroku que tenemos un contenedor con:
	heroku stack:set container -a contenedor-citas

Actualizamos:
	git push heroku master

(A mi me daba un error y lo arreglé con lo siguiente):
	heroku git:remote -a contenedor-proyecciones

Y de nuevo:
	git push heroku master

