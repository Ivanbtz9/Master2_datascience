#!/bin/env python3

import os, sys, time
import logging
import datetime
import threading
import asyncio
import numpy.random as npr


#Données temporelles
y = datetime.datetime.now().year
mo = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
m = datetime.datetime.now().minute
s = datetime.datetime.now().second


#Lance le chrono
t0 = time.time()


# Spécifiez le chemin du dossier que vous souhaitez créer
dossier = "log"

# Utilisez os.makedirs() pour créer le dossier s'il n'existe pas
# L'argument exist_ok=True permet de ne pas lever d'erreur si le dossier existe déjà
os.makedirs(dossier, exist_ok=True)

#créer un fichier log_temps dans le dossier log 
logging.basicConfig(filename=f'log/execution_asyncio_{y}-{mo}-{d}_{h}-{m}-{s}',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Verb:
    v = 0
    def __init__(self,v):
        Verb.v = v
    


class Accessoire(Verb):
    def __init__(self):
        self.liste_attente = []
    
    def __str__(self): #méthode str pour les print des instances
        if Verb.v == 2:
            return f"[{self.__class__.__name__}] état=  [{' , '.join(self.liste_attente)}]"#permet de créer un str avec une liste de str
        else:
            return ""

    def ajouter(self,elt): # Méthode de la classe mère pour ajouter un elt
        if elt == None:
            pass
        else:
            self.liste_attente.append(elt)
            logging.info(f'[{self.__class__.__name__}] fonction ajouter utilisée au temps {time.time()-t0}')
        
    
    def retirer(self): # Méthode de la classe mère pour retirer un elt
        if len(self.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction retirer utilisée au temps {time.time()-t0}')
            return self.liste_attente.pop()
        else:
            return None


class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    

    def __init__(self,temps_commande,temps_service):
        super().__init__()
        #Le pic stock les infos temps du serveur
        self.tc = temps_commande
        self.ts = temps_service

    def embrocher(self,postit):
        super().ajouter(postit)
        
    def liberer(self):
        return super().retirer()

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux/commandes, et évacuer le dernier reçu """
    def __init__(self,temps_preparation):
        super().__init__()
        #Le bar stock les infos temps du barman
        self.tp = temps_preparation
        self.encaisser = []

    def recevoir(self,plateau):
        super().ajouter(plateau)

    def evacuer(self):
        return super().retirer()

class Serveur(Verb,threading.Thread):
    def __init__(self,pic,bar,commandes):
        threading.Thread.__init__(self)
        print(f"[{self.__class__.__name__}] prêt pour le service")
        #faire un test pour vérifier que les objets donnés sont les bons
        if  isinstance(pic,Pic):
            self.pic = pic #fait le lien avec le pic
        else:
            raise ClasseInvalideError("La classe de pic n'est pas bonne" )
        if  isinstance(bar,Bar):
            self.bar = bar #fait le lien avec le bar
        else:
            raise ClasseInvalideError("La classe de bar n'est pas bonne" )
        self.commandes = commandes
        self.verrou = threading.Lock()

    async def prendre_commande(self):

        if len(self.commandes) ==0: 
            print("Il n'y a pas de commande, le bar ferme")
            sys.exit() #permet d'arreter le programme s'il n'y a pas de commande
        else:
            while len(self.commandes)>=1:
                c = self.commandes.pop(0) #retire le premier elt de la liste et le renvoi
                if c == None:
                    break
                else:
                    print(f'[{self.__class__.__name__}] je prends commande de {c}') 
                    logging.info(f'[{self.__class__.__name__}] fonction prendre_commande utilisée au temps {time.time()-t0}')
                    await asyncio.sleep(self.pic.tc)#temps de commande
                    if (Verb.v ==1) or (Verb.v ==2):
                        print(f"[{self.pic.__class__.__name__}] post-it '{c}' embroché")
                    self.verrou.acquire()
                    self.pic.embrocher(c)
                    self.verrou.release()
                    print(self.pic)
                if len(self.commandes)==0:
                    print(f"[{self.__class__.__name__}] il n'y a plus de commande à prendre")
        
    async def servir(self):
        try:
            while True:
                await asyncio.sleep(self.bar.tp )
                self.verrou.acquire()
                c = self.bar.evacuer() 
                self.verrou.release()
                if c == None:
                    continue
                else:
                    if (Verb.v ==1) or (Verb.v ==2):
                        print(f"[{self.bar.__class__.__name__}] '{c}' évacué")
                    print(self.bar)
                    if len(self.bar.liste_attente) == 0:
                        print(self.bar,'\nBar est vide') 
                    logging.info(f'[{self.__class__.__name__}] fonction servir utilisée au temps {time.time()-t0}')
                    await asyncio.sleep(self.pic.ts)
                    print(f'[{self.__class__.__name__}] je sers {c}')
        except KeyboardInterrupt:
            print("Arrêt manuel par l'utilisateur.")
            sys.exit() 
                
        
    async def run_serveur(self):
        loop_serveur = asyncio.new_event_loop() # créer une nouvelle boucle asyncio spécifique à chaque thread. Chaque thread doit avoir sa propre boucle asyncio
        asyncio.set_event_loop(loop_serveur) # indiquez à Python quelle boucle asyncio doit être utilisée pour gérer les opérations asynchrones dans le thread actuel
        asyncio.gather(self.prendre_commande(), self.servir())
            
            
            
            
                          

class Barman(Verb,threading.Thread): 
    def __init__(self,pic,bar):
        threading.Thread.__init__(self)
        print(f"[{self.__class__.__name__}] prêt pour le service !")
        self.pic = pic
        self.bar = bar
        self.verrou = threading.Lock()
        

    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        try:
            while True:
                self.verrou.acquire()
                c = self.pic.liberer()
                self.verrou.release()
                if c == None:
                    time.sleep(self.pic.tc)
                else:
                    if (Verb.v ==1) or (Verb.v ==2):
                        print(f"[{self.pic.__class__.__name__}] post-it '{c}' libéré")
                    if len(self.pic.liste_attente) == 0:
                        print(self.pic,'\nPic est vide')
                    else: 
                        print(self.pic)
                    print(f'[{self.__class__.__name__}] je commence la fabrication de {c}')
                    await asyncio.sleep(self.bar.tp)
                    logging.info(f'[{self.__class__.__name__}] fonction prepare utilisée au temps {time.time()-t0}')
                    print(f'[{self.__class__.__name__}] je termine la fabrication de {c}')
                    self.verrou.acquire()
                    self.bar.recevoir(c)
                    self.bar.encaisser.append(c)
                    self.verrou.release()
                    if (Verb.v ==1) or (Verb.v ==2):
                        print(f"[{self.bar.__class__.__name__}] '{c}' reçu")
                    print(self.bar)
        except KeyboardInterrupt:
            print("Arrêt manuel par l'utilisateur.")
            sys.exit() 

    async def encaisser(self):
        while True:
            if len(self.bar.encaisser)>=1:
                self.verrou.acquire()
                c = self.bar.encaisser.pop()
                self.verrou.release()
                tconso = 1 
                await asyncio.sleep(self.pic.ts + tconso )
                print(f"J'encaisse la commande {c}")
                logging.info(f'[{self.__class__.__name__}] fonction encaissée utilisée au temps {time.time()-t0}')
            
                
    async def run_barman(self):
        loop_barman = asyncio.new_event_loop() # créer une nouvelle boucle asyncio spécifique à chaque thread. Chaque thread doit avoir sa propre boucle asyncio
        asyncio.set_event_loop(loop_barman) # indiquez à Python quelle boucle asyncio doit être utilisée pour gérer les opérations asynchrones dans le thread actuel
        await asyncio.gather(self.encaisser(), self.preparer())



# Fermeture du gestionnaire de journalisation 
logging.shutdown()
