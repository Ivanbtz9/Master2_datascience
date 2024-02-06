# Introduction

Nous proposons un programme python qui récupère un fichier texte avec les associations possibles entre des pages webs numérotées et leur associe un Pagerank. Cet algorithme est inspiré de l'algorithme de Google pour le classement des pages webs lors d'une recherche sur un moteur de recherche.

Fichier : "soc-Epinions1.txt"

La colonne de gauche correspond aux numéros des pages webs et la colonne de droite correspond aux pages webs atteignables.
Nous avons construit un petit échantillon test pour les manipulations et les rendus des fonctions de notre programme.
Nous l'avons nommé "test.txt"

# Exécution du code

Pour exécuter le programme python, il vous suffit d'ouvrir un terminal linux à l'emplacement du programme et des données, vous devez ensuite entrer la commande suivante:

./ivanhoe_youness.py test.txt > rendu.txt

Le résultat du programme sera enregistré dans un fichier texte dans le même répertoire. Vous pourrez ensuite le consulter.

# Les étapes:


## mapper1: récupère chaque ligne et rends en clé la colonne de gauche et en valeur la colonne de droite.

rendu : 

"12"    "4"
"5"     "4"
"7"     "8"
"8"     "0"
...

## reducer1: classe par clée, page mère et renvoie une clée None et une valeur liste avec la page, son nombre de fille(s) et ses filles dans une liste.

rendu :

null    ["4", 3, ["1", "10", "12"]]
null    ["5", 4, ["0", "1", "2", "4"]]
null    ["7", 1, ["8"]]
null    ["8", 2, ["0", "5"]]
null    ["9", 2, ["0", "10"]]
null    ["0", 5, ["4", "5", "7", "8", "9"]]

## reducer2: permet de compter les pages parentes au total et de stocker cette valeur dans une variable de classe, elle renvoie ensuite une clée page_i et une valeur du type liste. 

rendu :

"8"     [2, ["0", "5"]]
"9"     [2, ["0", "10"]]
"0"     [5, ["4", "5", "7", "8", "9"]]
"10"    [5, ["1", "2", "4", "7", "9"]]

## mapper3 : rajoute seulement le PageRank à létape 0 dans la liste valeur

rendu:

"8"     [2, 0.1111111111111111, ["0", "5"]]
"9"     [2, 0.1111111111111111, ["0", "10"]]
"12"    [4, 0.1111111111111111, ["0", "2", "4", "5"]]
"10"    [5, 0.1111111111111111, ["1", "2", "4", "7", "9"]]

## mapperT :  Permets d'afficher les lignes précédentes et permets aussi d'affiche la contribution du parent pour chacun de ses enfants s'ils existent. 

rendu :

"12"    [4, 0.1111111111111111, ["0", "2", "4", "5"]]
"0"     0.02361111111111111
"2"     0.02361111111111111
"4"     0.02361111111111111
"5"     0.02361111111111111
"10"    [5, 0.1111111111111111, ["1", "2", "4", "7", "9"]]
"1"     0.018888888888888886
"2"     0.018888888888888886
"4"     0.018888888888888886
"7"     0.018888888888888886
"9"     0.018888888888888886

## reducerT : permet de regrouper par page et de calculer le nouveau PageRank en gardant le même format visuel qui était présent avant mapperT.
Le deuxième coefficient de la liste valeur est le nouveau PageRank. 

rendu : 

"8"     [2, 0.13, ["0", "5"]]
"0"     [5, 0.17407407407407405, ["4", "5", "7", "8", "9"]]
"9"     [2, 0.054444444444444434, ["0", "10"]]
"4"     [3, 0.11740740740740739, ["1", "10", "12"]]
"1"     [0, 0.10638888888888888, []]
"10"    [5, 0.09537037037037036, ["1", "2", "4", "7", "9"]]
"11"    [6, 0.016666666666666666, ["0", "1", "2", "4", "5", "6"]]
"12"    [4, 0.04814814814814815, ["0", "2", "4", "5"]]

## Le T est pour turn car nous avons répéter ce procédé 10 fois comme demandé. 

*[MRStep(mapper=self.mapperT,reducer=self.reducerT) for i in range(10)]

à mettre dans la fonction step. 

## mapper4 et reducer4 permettent de trier selon le PageRank et de faire un rendu visuel

rendu : 

"0.05106661052036747 est le PageRank de La page: "      "2"
"0.05330303842191271 est le PageRank de La page: "      "10"
"0.06242525170552944 est le PageRank de La page: "      "1"
"0.06628930243047011 est le PageRank de La page: "      "4"
"0.0671448579317814 est le PageRank de La page: "       "8"
"0.07077701738162853 est le PageRank de La page: "      "5"
"0.08840983904044092 est le PageRank de La page: "      "0"


# Le résultat avec le fichier final est :

......
"0.0013268408133847243 est le PageRank de La page: "    "401"
"0.0013630156825594464 est le PageRank de La page: "    "849"
"0.0013700101538133647 est le PageRank de La page: "    "725"
"0.0014158021373581948 est le PageRank de La page: "    "1619"
"0.0016782180440522289 est le PageRank de La page: "    "40"
"0.001794845431323114 est le PageRank de La page: "     "143"
"0.0018110930291383627 est le PageRank de La page: "    "790"
"0.0018272540419373483 est le PageRank de La page: "    "136"
"0.0019137817548184445 est le PageRank de La page: "    "1719"
"0.0019519409126113705 est le PageRank de La page: "    "118"
"0.0028944517178041405 est le PageRank de La page: "    "737"
"0.004158030644579244 est le PageRank de La page: "     "18"

Temps d'exécutiondu programme :  86.10992646217346 secondes