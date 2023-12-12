#!/bin/env python3

import os, sys, time
import numpy as np 
from bar_threading import *



 


if __name__ == "__main__":

    try:
        temps_commande = float(input('entrer un temps commande : \n'))
        temps_service = float(input('entrer un temps de service : \n'))
        temps_preparation = float(input('entrer un temps de preparation: \n'))
        v= int(input('entrer un niveau de verbosité entre 0 et 2 : \n'))
        while v not in range(3):
            v= int(input('Choisir entre 0, 1 et 2 : \n'))
    except:
        print('Vous devez entrer des nombres pour les temps\nRelancez le programme en respectant cette règle')
        sys.exit()
    commandes = sys.argv[1:] # ['Commande 1', 'Commande 2', 'Commande 3','Commande 4']# ,'Commande 5', 'Commande 6']  # 
    temps_de_travail = (len(commandes)+1)*(temps_preparation + temps_commande + temps_service)
    Verbosite = Verb(v)    
    pic = Pic(temps_commande,temps_service)
    bar = Bar(temps_preparation,temps_de_travail)
    

    serveur = Serveur(pic, bar, commandes)
    barman = Barman(pic, bar)

    
    serveur.start()
    barman.start()

    
