**********************
Contribuer avec GitHub
**********************

.. warning::

    Aucun commit n'est réalisé directement sur le dépot principal du projet
    (https://github.com/PnX-SI/GeoNature-citizen). Pour contribuer, il est
    nécessaire de faire un *fork* du projet, de travailler sur un fork et
    sur une nouvelle branche basée sur la branche ``dev`` du dépot principal.

Faire un ticket pour discuter de votre projet de modification
#############################################################

Il est fortement recommandé de réaliser préalablement un ticket pour discuter
avec la communauté des développeurs et utilisateurs de votre projet.


Faire un fork du projet
#######################

`Tout est ici <https://help.github.com/articles/fork-a-repo/>`_


Cloner localement le projet
###########################

Dans un terminal:

.. code-block:: bash

    $ git clone git@github.com:YOUR_NAME/GeoNature-citizen.git

    Cloning into `GeoNature-citizen`...
    remote: Counting objects: 10, done.
    remote: Compressing objects: 100% (8/8), done.
    remove: Total 10 (delta 1), reused 10 (delta 1)
    Unpacking objects: 100% (10/10), done.

Récupérer les mises à jour du dépot principal
*********************************************

Dans un terminal, dans le dossier cloné:

.. code-block:: bash

    $ git remote add upstream git@github.com:PnX-SI/GeoNature-citizen.git

Pour vérifier que votre clone local puisse suivre votre
dépot (*origin*) et le dépot principal (*upstream*):

.. code-block:: bash

    $ git remove -v

    origin	git@github.com:YOUR_NAME/GeoNature-citizen.git (fetch)
    origin	git@github.com:YOUR_NAME/GeoNature-citizen.git (push)
    upstream	git@github.com:PnX-SI/GeoNature-citizen.git (fetch)
    upstream	git@github.com:PnX-SI/GeoNature-citizen.git (push)

Créer votre propre branche de développement
*******************************************

Pour créer votre branche de développement, dans un terminal:

.. code-block:: bash

    $ git checkout -b dev_mabranche


Créer une pull-request de vos modifications
*******************************************

Une fois vos modifications apportées, réalisez une pull-request
sur la branche ``dev`` du dépot principal en y mentionnant le ticket concerné.
