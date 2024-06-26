******************************************
Configurer et installer la base de données
******************************************

GeoNature-citizen s'appuie sur le serveur de base de données spatiales \
PostgreSQL et son extension spatiale PostGIS.


Installer le serveur
####################

Pour installer le serveur de base de données, suiviz les \
instructions du site officiel \
`PostgreSQL Downloads <https://www.postgresql.org/download/>`_:

Concrètement, sur Debian et ubuntu:

.. code:: sh

    sudo apt update
    sudo apt install postgis

Configurer la base de données
#############################

Création du role principal
**************************

Pour créer la base de données spatiale. On considèrera ici que l'utilisateur \
de la base de données sera ``dbuser``, renseignez alors le mot de passe de \
l'utilisateur lorsqu'il vous sera demandé :

.. code:: sh

    sudo -u postgres createuser -e -E -P dbuser

Créez la base de données, ici nommée ``geonaturedb`` appartenant à l'utilisateur ``dbuser``:

Création de la base de données et des extensions
************************************************

.. code:: sh

    sudo -u postgres createdb -e -E UTF8 -O dbuser geonaturedb

Activez les extensions ``postgis`` pour la gestion des données spatiales et ``uuid-ossp`` \
pour la gestion des uuid. Seul un superutilisateur peut activer les extensions (ici, \
l'utilisateur ``postgres``, installé par défaut) :

.. code:: sh

    sudo -u postgres psql geonaturedb -c 'create extension postgis; create extension "uuid-ossp";'

Votre serveur de base de données est maintenant opérationel.
