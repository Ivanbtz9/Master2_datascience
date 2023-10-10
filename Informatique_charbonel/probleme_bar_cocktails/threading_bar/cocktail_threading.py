#!/bin/env python3

import os, sys, time
import numpy as np 
from bar_threading import *



 


if __name__ == "__main__":

    try:
        temps_commande = 1#float(input('entrer un temps commande : \n'))
        temps_service = 1#loat(input('entrer un temps de service : \n'))
        temps_preparation = 1#float(input('entrer un temps de preparation: \n'))
        v= 0#int(input('entrer un niveau de verbosité entre 0 et 2 : \n'))
        while v not in range(3):
            v= int(input('Choisir entre 0, 1 et 2 : \n'))
    except:
        print('Vous devez entrer des nombres pour les temps\nRelancez le programme en respectant cette règle')
        sys.exit()

    
    Verbosite = Verb(v)    
    pic = Pic(temps_commande,temps_service)
    bar = Bar(temps_preparation)
    commandes = ['Commande 1', 'Commande 2', 'Commande 3','Commande 4']# ,'Commande 5', 'Commande 6']  #sys.argv[1:] #  

    serveur = Serveur(pic, bar, commandes)
    barman = Barman(pic, bar)

    asyncio.run(serveur.run_serveur())
    asyncio.run(barman.run_barman())





    
    


    
           
        




 








