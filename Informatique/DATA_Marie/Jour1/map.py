#! /usr/bin/env python3

import sys
import re

motif=re.compile("\w+") 


for ligne in sys.stdin: 
    liste_mots = motif.findall(ligne.strip().lower())
    for mot in set(liste_mots) :
        print(f"{mot}\t{liste_mots.count(mot)}")