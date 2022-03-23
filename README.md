[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet Fil Rouge MS SIO Simon ADDA 

Objectifs:

Étudier et développer l'ensemble d'une chaîne de traitements en Python, de la collecte des données en passant par la validation, la reconnaissance d'entités nommées, la mise en relation, la restitution, la déduction de  nouvelles données, l'interrogation, la représentation de la connaissance produite. Être en mesure d'apporter un indicateur de la qualité et de la précision de la chaîne de traitement fait partie des objectifs

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)

## Presentation du projet:

### Service Ontology:

- PFR.ipynb: Dans ce fichier sous jupyter notebook, vous trouverez la chaine de traitement pour telecharger les pdf de Arvix, traiter les textes afin d'en extraire les entities nommées et enfin la creation d'une entology visible grace a Protegé.

### Service AWS:

- /AWS: Dans ce repertoire l'utilisation du service Comprehend de AWS. Ce dernier permet d'extraire les entites nommées d'un texte (Cours AWS).

        On y trouve un notebook que l'utilisateur doit executer cellules par cellules afin de voir les resultats.
        Dans le repertoire /Download on y trouve des fichier telecharger pour effectuer les tests du service dans le notebook.
        Dans le repertoire /Teacher, vous pouvez ajouter votre propre pdf. Une section dans le notebook explique les details.

### Service SOA:

- /app : Dans le repertoire /app, vous trouverez un API permettant d'analyser le contenu d'un texte avec NLTK. Deux services sont proposés:


    Exemple : 
    
    L'histoire de la France commence avec les premières occupations humaines du territoire correspondant au pays actuel. Aux groupes présents depuis le Paléolithique et le Néolithique, sont venues s'ajouter, des peuples germains (Francs, Wisigoths, Alamans, Burgondes) et au ixe siècle de scandinaves appelés Normands.

- GET NLTK/Tag : Permet d'extraire les tags d'un texte:

        curl -X 'GET' \ 'http://127.0.0.1/NLTK/Tag text=L%27histoire%20de%20la%20France%20commence%20avec%20les%20premi%C3%A8res%20occupations%20humaines%20du%20territoire%20correspondant%20au%20pays%20actuel.%20Aux%20groupes%20pr%C3%A9sents%20depuis%20le%20Pal%C3%A9olithique%20et%20le%20N%C3%A9olithique%2C%20sont%20venues%20s%27ajouter%2C%20des%20peuples%20germains%20%28Francs%2C%20Wisigoths%2C%20Alamans%2C%20Burgondes%29%20et%20au%20ixe%20si%C3%A8cle%20de%20scandinaves%20appel%C3%A9s%20Normands.' \
        -H 'accept: application/json'

        Response Body:
        {
        "Tag in text from NLTK ": [
            [
            [
                "L'histoire",
                "NNP"
            ],
            [
                "de",
                "NNP"
            ],
            [
                "la",
                "FW"
            ],
            [
                "France",
                "NNP"
            ],
            [
                "commence",
                "NN"
            ],
            [
                "avec",
                "NN"
            ] ...
        ]
        }


- GET NLTK/NER: Permet d'extraire les entitées nommées d'un texte
	
        Response body:
        {
        "Names entities in text from NLTK ": [
            "Francs",
            "Normands",
            "Alamans",
            "Wisigoths",
            "Burgondes",
            "France"
        ]
        }


Interactive API docs: 

Now you can go to http://127.0.0.1/docs and try the API to analyse a text.

### Service Docker:

Go in the main folder and type to build the image:

    docker build -t pfr .

Then this line to run the container:

    docker run -d --name mycontainer -p 80:80 pfr

Interactive API docs: 

Now you can go to http://127.0.0.1/docs and try the API to analyse a text.

## Installation 

For PFR.ipynb: Open the conda terminal in your env:

    conda install -c conda-forge poppler

You can now open PFR.ipynb and excute it.

### Application : Only for AWS, SOA and Hadoop services (on Ubuntu or MacOs):

Create a virtual environment and activate it:

    python3 -m venv venv
    . venv/bin/activate

Install arXiv Intelligence:

    pip install -r requirements.txt
