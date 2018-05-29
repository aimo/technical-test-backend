# Creación de un API REST

La prueba consistirá en crear un simple API REST para un único recurso, la prueba se dividirá en una funcionalidad básica y en funcionalidades adicionales que sumarán puntos a la evaluación. 

Este repositorio contiene los archivos base, los cambios realizados deben subirse en un repositorio propio, el link de ese repositorio debe enviarse por email.

## 1. Funcionalidad básica
Se desea un endpoint para poder administrar **notas** (crear y listar), los datos se guardará en una base de datos **sqlite**. Para ello se utilizarán los siguientes paquetes de Python.
* [peewee](http://docs.peewee-orm.com/en/latest/ "peewee") (ORM)
* [bottle](https://bottlepy.org/docs/dev/ "bottle") (miniframework web)

Los campos que tendrá el modelo no son relevantes.

## 2. Funcionalidades adicionales
Las siguientes funcionalidades se construirán sobre la funcionalidad base.

**Serialización y validación**

Se desea validar los datos que se reciben via POST y mostrar los errores al usuario que usa el API, serializar la lista de objetos para enviarlas como json. Para ello se utilizará la librería [marshmallow](https://marshmallow.readthedocs.io/en/latest/ "marshmallow").

**Usuario y Autentificación**

Se desea que el API sea restringido mediante algún método de autenficación.

**JWT**

Se desea que el usuario se autentifique mediante json web tokens, para ello se utializará la librería [pyjwt](https://github.com/jpadilla/pyjwt "pyjwt")

**Autorización**

Se desea asociar una **nota** con un **usuario**, de tal manera que cada usuario solo pueda ver sus propias notas.

**Cliente del API**

Se desea tener un cliente web que haga uso del API desde frontend (html y javascript). Ver siguiente sección.

# Estructura de archivos
El repositorio contiene archivos que sirven como guia, pero se deja la libertad de hacer los cambios que se consideren necesarios.
* **.gitignore** - Archivos ignorados por git, añadir la base de datos sqlite que se genere.
* **requirements.txt** - Los paquetes python que se utilizarán para la prueba. Se recomienda usar un entorno virtual (ejem. [virtualenv](https://virtualenv.pypa.io/en/stable/ "virtualenv")) para instalarlos.
* **server.py** - Contendrá tóda la lógica del api, este correrá en el puerto 8000.
* **client.py** - Un pequeño servidor que corre en el puerto 5000 y sirve el archivo index.html, aquí no se necesita hacer ninguna modificación.
* **index.html** - Donde idealmente deberá estar toda la lógica para loguearse y mostrar los datos del api.

# Objetivos de la prueba
* Evaluar el conocimiento general del lenguaje Python.
* Evaluar el conocimiento en arquitecturas web (MVC, REST).
* Comprobar el conocimiento independientemente de la herramienta / framework.
* Evaluar buenas prácticas en el código relacionadas con Python (pep8).
* Evaluar conocimientos basicos de frontend.
* Evaluar el modelo mental que se tiene para la organización de classes, funciones, módulos.
