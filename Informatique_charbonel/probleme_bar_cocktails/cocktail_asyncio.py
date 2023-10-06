#!/bin/env python3

import os, sys, time
import numpy as np 
from bar_asyncio import *
import asyncio

async def main():
    try:
        temps_commande = float(input('entrer un temps commande : \n'))
        temps_service = float(input('entrer un temps de service : \n'))
        temps_preparation = float(input('entrer un temps de preparation: \n'))
    except:
        print('Vous devez entrer des nombres pour les temps\nRelancez le programme en respectant cette règle')
        sys.exit()
        
    pic = Pic(temps_commande,temps_service)
    bar = Bar(temps_preparation)
    commandes = sys.argv[1:] # ['Commande 1', 'Commande 2', 'Commande 3','Commande 4', 'Commande 5', 'Commande 6']  

    serveur = Serveur(pic, bar, commandes)
    barman = Barman(pic, bar)

    
    # Démarrez les tâches asynchrones
    tasks3 = [serveur.prendre_commande(),serveur.servir(),barman.preparer()]
    

    await asyncio.gather(*tasks3) #gère la concurrence 



if __name__ == "__main__":
    asyncio.run(main())




 








