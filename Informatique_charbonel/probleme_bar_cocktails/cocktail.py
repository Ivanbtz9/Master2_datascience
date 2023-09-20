#!/bin/env python3

import os, sys, time
import numpy as np 

liste_commandes = sys.argv[1:]
#print(liste_cocktail)

for i in range(len(liste_commandes)):
    liste_commandes[i] = liste_commandes[i].split('+')



