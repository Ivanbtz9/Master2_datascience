#!/bin/env python3

import os, sys, time
import numpy as np 
from bar_asyncio import *
import asyncio

async def main():
    pic = Pic()
    bar = Bar()
    commandes = ['Commande 1', 'Commande 2', 'Commande 3','Commande 4', 'Commande 5', 'Commande 6']  #sys.argv[1:] 
    serveur = Serveur(pic, bar, commandes)
    barman = Barman(pic, bar)

    
    # Démarrez les tâches asynchrones
    #tasks1 = [serveur.prendre_commande(), barman.preparer()]
    #tasks2 = [barman.preparer(),serveur.servir()]
    tasks3 = [serveur.servir(),serveur.prendre_commande(),barman.preparer()]

    #await asyncio.gather(*tasks1) #gère la concurrence au niveau du pic
    #print(bar)
    #await asyncio.gather(*tasks2) #gère la concurrence au niveau du bar
    #print(bar)
    await asyncio.gather(*tasks3) #gère la concurrence 



if __name__ == "__main__":
    asyncio.run(main())













