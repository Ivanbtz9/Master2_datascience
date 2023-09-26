#!/bin/env python3

import os, sys, time
import logging


logging.basicConfig(filename=f'log/execution_{time.time()}',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

t0 = time.time()

class Accessoire:
    def __init__(self):
        self.liste_attente = []
    
    def __str__(self):
        return f"[{self.__class__.__name__}] état=  [{' , '.join(self.liste_attente)}]"#permet de créer un str avec une liste de str


class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """

    def __init__(self):
        super().__init__()

    def embrocher(self,postit):
        self.liste_attente.append(postit)
        logging.info(f'[{self.__class__.__name__}] fonction embrocher utilisée au temps {time.time()-t0}')
        
    def liberer(self):
        if len(self.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction liberer utilisée au temps {time.time()-t0}')
            return self.liste_attente.pop() #del(self.liste_attente[-1]) #on peut utiliser del mais plus long
        else:
            pass

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux/commandes, et évacuer le dernier reçu """
    def __init__(self):
        super().__init__()

    def recevoir(self,plateau):
        logging.info(f'[{self.__class__.__name__}] fonction recevoir utilisée au temps {time.time()-t0}')
        self.liste_attente.append(plateau)

    def evacuer(self):
        if len(self.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction evacuer utilisée au temps {time.time()-t0}')
            return self.liste_attente.pop() #del(self.liste_attente[-1]) #on peut utiliser del mais plus long
        else:
            pass

class Serveur:
    def __init__(self,pic,bar,commandes):
        print(f"[{self.__class__.__name__}] prêt pour le service")
        if  isinstance(pic,Pic):
            self.pic = pic
        else:
            raise ClasseInvalideError("La classe de pic n'est pas bonne" )
        if  isinstance(bar,Bar):
            self.bar = bar
        else:
            raise ClasseInvalideError("La classe de bar n'est pas bonne" )
        self.commandes = commandes

    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        while len(self.commandes)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction prendre_commande utilisée au temps {time.time()-t0}')
            c = self.commandes.pop()
            print(f'[{self.__class__.__name__}] je prends commande de {c}')
            time.sleep(1)
            self.pic.embrocher(c)
            print(f"[{self.pic.__class__.__name__}] post-it '{c}' embroché")
            print(self.pic)
            if len(self.commandes)==0:
                print(f"[{self.__class__.__name__}] il n'y a plus de commande à prendre")
        

           
    def servir(self):
        """ Prend un plateau sur le bar. """
        while len(self.bar.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction servir utilisée au temps {time.time()-t0}')
            print(self.bar)
            c = self.bar.liste_attente.pop()
            print(f"[{self.bar.__class__.__name__}] '{c}' évacué")
            time.sleep(1)
            print(f'[{self.__class__.__name__}] je sers {c}')
            if len(self.bar.liste_attente) == 0:
                print(self.bar,'\nBar est vide')
        

       

class Barman:
    def __init__(self,pic,bar):
        print(f"[{self.__class__.__name__}] prêt pour le service !")
        self.pic = pic
        self.bar = bar

    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        while len(self.pic.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction prepare utilisée au temps {time.time()-t0}')
            print(self.pic)
            c = self.pic.liste_attente[-1]
            self.pic.liberer()
            print(f"[{self.pic.__class__.__name__}] post-it '{c}' libéré")
            print(f'[{self.__class__.__name__}] je commence la fabrication de {c}')
            time.sleep(1)
            print(f'[{self.__class__.__name__}] je termine la fabrication de {c}')
            self.bar.recevoir(c)
            print(f"[{self.bar.__class__.__name__}] '{c}' reçu")
            print(self.bar)
            if len(self.pic.liste_attente) == 0:
                print(self.pic,'\nPic est vide')


# Fermeture du gestionnaire de journalisation 
logging.shutdown()
