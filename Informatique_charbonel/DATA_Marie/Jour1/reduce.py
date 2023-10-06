#! /usr/bin/env python3

import sys
import re

cle_pre = None
compteur = 0

for ligne in sys.stdin:
    cle , valeur = ligne.strip().split("\t")
    if cle == cle_pre:
        compteur += int(valeur)
    else:
        if cle_pre == None:
            cle_pre = cle
        else:
            print(cle_pre, compteur)
            cle_pre = cle






     