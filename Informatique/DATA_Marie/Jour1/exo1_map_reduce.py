#! /usr/bin/env python3

import json
import os
import pprint
import csv
import pandas as pd
import sys
import re

motif=re.compile("\w+") #motif d'un mot


for ligne in sys.stdin: #sys.stdin permets une interaction avec les ligne de commandes
    liste_mots = motif.findall(ligne.strip().lower())
    for mot in set(liste_mots) :
        print(f"{mot}\t{liste_mots.count(mot)}")


"""strip(): Cette méthode permet de supprimer les caractères blancs 
(espaces, tabulations, sauts de ligne, etc.) situés à la fois au début et à la fin de la chaîne.
    Cela aide à éliminer les espaces inutiles qui pourraient entourer la chaîne et à la rendre plus propre.

lower(): Cette méthode convertit tous les caractères de la chaîne en minuscules.
    Cela permet de normaliser la casse (majuscules/minuscules) des caractères, ce qui facilite la comparaison et
    la recherche dans le texte sans se soucier de la casse."""

