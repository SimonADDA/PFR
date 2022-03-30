[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet Fil Rouge MS SIO Simon ADDA 

Objectifs:

Étudier et développer l'ensemble d'une chaîne de traitements en Python, de la collecte des données en passant par la validation, la reconnaissance d'entités nommées, la mise en relation, la restitution, la déduction de  nouvelles données, l'interrogation, la représentation de la connaissance produite. Être en mesure d'apporter un indicateur de la qualité et de la précision de la chaîne de traitement fait partie des objectifs

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)


#### Installation:

Create a virtual environment and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install requirements:

    $ pip install -r requirements.txt

## Presentation du projet:

### Service AWS:

- /AWS: Dans ce repertoire l'utilisation du service Comprehend de AWS. Ce dernier permet d'extraire les entites nommées d'un texte (Cours AWS).

On y trouve deux script python et un notebook que l'utilisateur peut executer cellules par cellules afin de voir les resultats en details (AWS_service.ipynb).

Pour tester avec des pdfs deja fourni, executez simplement cette commande:

        $ python3 AWS/AWS_Exemple.py

Les resultats se trouves dans le fichiers json : /Download/EntitiesPDF.json

Pour votre propre pdf, ajoutez ce dernier dans le repertoire Professeur et executez cette commande:

        $ python3 AWS/AWS_Teacher.py

Les resultats se trouves dans le fichiers json : /Professeur/AWS_json_teacher.json
