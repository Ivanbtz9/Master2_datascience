#!/bin/env python3

import os, sys, time
import numpy as np 


class Accessoire:
    def __init__(self):
        self.liste_attente = []
    
    def __str__(self):
        return self.liste_attente


class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """

    def __init__(self):
        super().__init__()

    def embrocher(self,postit):
        pass
        
    def liberer(self):
        return postit

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux/commandes, et évacuer le dernier reçu """
    def __init__(self):
        super().__init__()

    def recevoir(self,plateau):
        pass
    def evacuer(self):
        return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        pass
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        pass
    def servir(self):
        """ Prend un plateau sur le bar. """
        pass

class Barman:
    def __init__(self,pic,bar):
        self
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        self 