#MODULES

Vérifier que les modules suivants sont bien installés sur votre machine.

- os
- sys
- time
- asyncio
- logging
- datetime 

Dans le cas contraire lancer la commande suivante dans un terminal Linux 

pip3 install module 

# Execution

Placer les deux fichiers .py dans un même répertoire et en ouvrant un terminal vous pouvez lancer le programme main.py de la manière suivante par exemple:

./cocktail_asyncio.py 'Commande 1' 'Commande 2' 'Commande 3' 'Commande 4' 'Commande 5' 'Commande 6'

Entrer un temps de commande, un temps de préparation et un temps de service 

exemple: 

entrer un temps commande : 
1
entrer un temps de service : 
2
entrer un temps de preparation: 
0.5

La sortie dans ce cas est la suivante : 

[Serveur] prêt pour le service
[Barman] prêt pour le service !
[Serveur] je prends commande de Commande 1
[Pic] post-it 'Commande 1' embroché
[Pic] état=  [Commande 1]
[Serveur] je prends commande de Commande 2
[Pic] post-it 'Commande 1' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 1
[Barman] je termine la fabrication de Commande 1
[Bar] 'Commande 1' reçu
[Bar] état=  [Commande 1]
[Bar] 'Commande 1' évacué
[Bar] état=  []
[Bar] état=  [] 
Bar est vide
[Pic] post-it 'Commande 2' embroché
[Pic] état=  [Commande 2]
[Serveur] je prends commande de Commande 3
[Pic] post-it 'Commande 2' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 2
[Pic] post-it 'Commande 3' embroché
[Pic] état=  [Commande 3]
[Serveur] je prends commande de Commande 4
[Barman] je termine la fabrication de Commande 2
[Bar] 'Commande 2' reçu
[Bar] état=  [Commande 2]
[Pic] post-it 'Commande 3' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 3
[Serveur] je sers Commande 1
[Bar] 'Commande 2' évacué
[Bar] état=  []
[Bar] état=  [] 
Bar est vide
[Barman] je termine la fabrication de Commande 3
[Bar] 'Commande 3' reçu
[Bar] état=  [Commande 3]
[Pic] post-it 'Commande 4' embroché
[Pic] état=  [Commande 4]
[Serveur] je prends commande de Commande 5
[Pic] post-it 'Commande 4' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 4
[Pic] post-it 'Commande 5' embroché
[Pic] état=  [Commande 5]
[Serveur] je prends commande de Commande 6
[Barman] je termine la fabrication de Commande 4
[Bar] 'Commande 4' reçu
[Bar] état=  [Commande 3 , Commande 4]
[Pic] post-it 'Commande 5' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 5
[Serveur] je sers Commande 2
[Bar] 'Commande 4' évacué
[Bar] état=  [Commande 3]
[Barman] je termine la fabrication de Commande 5
[Bar] 'Commande 5' reçu
[Bar] état=  [Commande 3 , Commande 5]
[Pic] post-it 'Commande 6' embroché
[Pic] état=  [Commande 6]
[Serveur] il n'y a plus de commande à prendre
[Pic] post-it 'Commande 6' libéré
[Pic] état=  [] 
Pic est vide
[Barman] je commence la fabrication de Commande 6
[Barman] je termine la fabrication de Commande 6
[Bar] 'Commande 6' reçu
[Bar] état=  [Commande 3 , Commande 5 , Commande 6]
[Serveur] je sers Commande 4
[Bar] 'Commande 6' évacué
[Bar] état=  [Commande 3 , Commande 5]
[Serveur] je sers Commande 6
[Bar] 'Commande 5' évacué
[Bar] état=  [Commande 3]
[Serveur] je sers Commande 5
[Bar] 'Commande 3' évacué
[Bar] état=  []
[Bar] état=  [] 
Bar est vide
[Serveur] je sers Commande 3

#Log

Un dossier Log se cré automatiquement dans lequel les fichiers log se crés à chaque exécution avec des informations sur les temps d'exécution des étapes 

#Bonnes commandes


## L'abus d'alcool est dangereux pour la santé à consommer avec modération




