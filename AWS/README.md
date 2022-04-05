[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet Fil Rouge MS SIO Simon ADDA 

**AWS service**

*Dans cette partie du projet vous trouverez l'utilisation du service Comprehend de AWS.*

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)


#### Installation:

Create a virtual environment and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install requirements:

    $ apt-get install gcc python-dev libkrb5-dev
    $ pip install -r requirements.txt

## Presentation du projet:

### Service AWS:

- /AWS: Dans ce repertoire l'utilisation du service Comprehend de AWS. Ce dernier permet d'extraire les entites nommées d'un texte (Cours AWS).

On y trouve deux scripts python et un notebook (que l'utilisateur peut executer cellules par cellules afin de voir les resultats en details AWS_service.ipynb).

Pour tester avec des pdfs deja fourni, executez simplement cette commande:

        $ python3 AWS/AWS_Exemple.py

Les resultats se trouves dans le fichiers json : **/Download/EntitiesPDF.json**

Pour votre propre pdf, **supprimez le pdf fourni "projetSIO2021-2022.pdf" dans /Professeur et ajoutez votre pdf dans ce meme repertoire** et executez cette commande:

        $ python3 AWS/AWS_Teacher.py

Les resultats se trouves dans le fichiers json : **/Professeur/AWS_json_teacher.json**
