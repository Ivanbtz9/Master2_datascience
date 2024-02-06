#!/bin/env python3

import os, sys, time
import numpy as np 
from bar import *



if __name__ == "__main__":
    liste_commandes = sys.argv[1:] #liste_commandes[i].split('+')
    Pic = Pic()
    Bar = Bar()
    Serveur = Serveur(Pic,Bar,commandes= liste_commandes)
    Barman = Barman(Pic,Bar)

    Serveur.prendre_commande()
    Barman.preparer()
    Serveur.servir()












