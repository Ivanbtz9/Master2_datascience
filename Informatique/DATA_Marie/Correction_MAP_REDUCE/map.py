#! /usr/bin/env python3

import sys
import re
motif=re.compile("\w+") #motif pour un mot
c=0

for ligne in sys.stdin: #permet de lire ce qui est transmis
    c+=1
    liste_mots = motif.findall(ligne.strip().lower())
    for mot in set(liste_mots) :
        print(f"{mot}\t{liste_mots.count(mot)}")

print(f"Le nombre de lignes est de {c}")