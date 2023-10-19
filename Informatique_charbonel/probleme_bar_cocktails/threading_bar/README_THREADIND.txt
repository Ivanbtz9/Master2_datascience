#MODULES

Vérifier que les modules suivants sont bien installés sur votre machine.

- os
- sys
- time
- threading
- logging
- datetime 


Dans le cas contraire lancer la commande suivante dans un terminal Linux

pip3 install module


# Execution

Placer les deux fichiers .py dans un même répertoire et en ouvrant un terminal vous pouvez lancer le programme principal de la manière suivante par exemple:

./cocktail_treading.py 'Commande 1' 'Commande 2' 'Commande 3' 'Commande 4' 'Commande 5' 'Commande 6'

Entrer un temps de commande, un temps de préparation et un temps de service

#Log

Un dossier Log se crée automatiquement dans lequel les fichiers log se créent à chaque exécution avec des informations sur les temps d'exécution des étapes


# Explication du code :

Le serveur et le barman vivent dans deux Threads différents et peuvent interagir à l'aide de certains attributs tels que le pic et le bar, ils sont créés au début du programme.
Le barman va toujours essayer de servir une commande avant d'en prendre une nouvelle, de même le barman va toujours essayer d'encaisser avant de faire une préparation.
Le serveur et le barman étant des hommes/femmes, ils ne peuvent pas faire plus qu'une chose à la fois. Rajouter de l'asynchronisme dans chacun des Threads semble être non réaliste.


### Axe d'amélioration,

Rajouter de l'asynchronisme dans la classe serveur pour simuler le temps de consommation de chaque client sans pour autant empêcher le serveur de travailler.
Idée non développée pour le moment. Les grands points seraient:

- Créer une classe client
- à chaque commande, créer un attributs client_i qui hériterait de la classe serveur. Les client_i serait stocké dans un dictionnaire chez le serveur.
- à chaque service lancé une fonction asynchrone clent_i.consommation() qui patiente et qui peut modifier la liste d'encaissement du bar et donner ainssi la possibilité
au barman d'encaisser le client_i


