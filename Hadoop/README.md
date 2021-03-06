[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Projet Fil Rouge MS SIO Simon ADDA 

*Dans cette partie vous trouverez des inforamtions sur l'export des metadata d'articles scientfiques vers HDFS.*

**Service Hadoop:**

- /Hadoop : Dans ce repertoire vous trouverez un fichier d'execution de code csv (write_csv.py) et un code d'ecriture dans le cluster (csv_to_hdfs.py).

## Pré-requis

Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)

### Installation:

Create a virtual environment and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install requirements:

    $ apt-get install gcc python-dev libkrb5-dev
    $ pip install -r requirements.txt


### Dans le venv:

#### Export scientific articles metadata to HDFS

Install the requirement

    $ sudo apt-get install gcc python-dev libkrb5-dev

#### Envoyer un ticket

    $ kinit s.adda-cs
    $ klist

#### Execution des fichiers python:

    $ python3 Hadoop/write_csv.py
    $ python3 Hadoop/csv_to_hdfs.py

#### Vérifier que la table est sur hdfs (dans la connexion ssh)

    $ hdfs dfs -ls /education/cs_2022_spring_1/s.adda-cs/PFR/

### Zeppelin: s.adda

http://zep-1.au.adaltas.cloud:9995/#/

![Graph Zeppelin](/Hadoop/Graph.PNG?raw=true "Graph Zeppelin")

