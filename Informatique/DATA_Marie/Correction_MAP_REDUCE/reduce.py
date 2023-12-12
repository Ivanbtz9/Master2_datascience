#! /usr/bin/env python3

import sys
import re

cle_prec,nb_tot = None,0

nb_phrases = re.compile("Le nombre de lignes est de ")

for ligne in sys.stdin:
    if nb_phrases.findall(ligne):
        print(ligne)

    else:
        cle,nb = ligne.split('\t')[0], int(ligne.split('\t')[1])
        if cle == cle_prec:
            nb_tot +=1
        elif cle_prec == None:
            cle_prec = cle
            nb_tot +=1
        else:
            print(nb_tot,cle_prec)
            cle_prec = cle
            nb_tot = nb
     



