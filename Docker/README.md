[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet Fil Rouge MS SIO Simon ADDA 

*Dans cette partie vous trouverez l'installation avec Docker de l'API (dans le dossier /app) avec FastAPI.*

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)


#### Installation:

Create a virtual environment and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install requirements:

    $ pip install -r requirements.txt


### Service Docker - API NLTK:

Go in the main folder and type to build the image:

    $ docker build -t pfr .

Then run the container:

    $ docker run -d --name mycontainer -p 80:80 pfr

Interactive API docs: 

Now you can go to http://127.0.0.1/docs and try the API to analyse a text.
