#!/bin/env python3

import os, sys, time
import logging
import asyncio
import datetime

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




class Accessoire:
    def __init__(self):
        self.liste_attente = []
    
    def __str__(self): #méthode str pour les print des instances
        return f"[{self.__class__.__name__}] état=  [{' , '.join(self.liste_attente)}]"#permet de créer un str avec une liste de str

    def ajouter(self,elt): # Méthode de la classe mère pour ajouter un elt
        self.liste_attente.append(elt)
        logging.info(f'[{self.__class__.__name__}] fonction ajouter utilisée au temps {time.time()-t0}')
        
    
    def retirer(self): # Méthode de la classe mère pour retirer un elt
        if len(self.liste_attente)>=1:
            logging.info(f'[{self.__class__.__name__}] fonction retirer utilisée au temps {time.time()-t0}')
            return self.liste_attente.pop()
        else:
            pass


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

    def recevoir(self,plateau):
        super().ajouter(plateau)

    def evacuer(self):
        return super().retirer()

class Serveur:
    def __init__(self,pic,bar,commandes):
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

    async def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """

        if len(self.commandes) ==0: 
            print("Il n'y a pas de commande, le bar ferme")
            sys.exit() #permet d'arreter le programme s'il n'y a pas de commande
        else:
            while len(self.commandes)>=1:
                c = self.commandes.pop(0) #retire le premier elt de la liste et le renvoi
                print(f'[{self.__class__.__name__}] je prends commande de {c}') 
                await asyncio.sleep(self.pic.tc)#temps de commande
                logging.info(f'[{self.__class__.__name__}] fonction prendre_commande utilisée au temps {time.time()-t0}')
                print(f"[{self.pic.__class__.__name__}] post-it '{c}' embroché")
                self.pic.embrocher(c)
                print(self.pic)
                if len(self.commandes)==0:
                    print(f"[{self.__class__.__name__}] il n'y a plus de commande à prendre")
        



    async def servir(self):
        """ Prend un plateau sur le bar. """
        
        

        while (len(self.bar.liste_attente)>=1) or (len(self.pic.liste_attente)>=1) or (len(self.commandes)>=1):
            c = self.bar.evacuer() #Renvoie une commande qui peut être un None
            if c == None:
                await asyncio.sleep(self.bar.tp ) # Attendre un peu la commande va arriver sur le bar 
            else:
                print(f"[{self.bar.__class__.__name__}] '{c}' évacué")
                print(self.bar)
                if len(self.bar.liste_attente) == 0:
                    print(self.bar,'\nBar est vide') 
                await asyncio.sleep(self.pic.ts)
                logging.info(f'[{self.__class__.__name__}] fonction servir utilisée au temps {time.time()-t0}')
                print(f'[{self.__class__.__name__}] je sers {c}')
            

        if len(self.pic.liste_attente)==0:
            #print('Dernière commande en cours de préparation par le barman il faut attendre la fin')
            await asyncio.sleep(self.bar.tp)
            c = self.bar.evacuer()
            if c == None:
                sys.exit()
            else:
                print(f"[{self.bar.__class__.__name__}] '{c}' évacué")
                print(self.bar,'\nBar est vide') 
                await asyncio.sleep(self.pic.ts)
                logging.info(f'[{self.__class__.__name__}] fonction servir utilisée au temps {time.time()-t0}')
                print(f'[{self.__class__.__name__}] je sers {c}')
                               

class Barman:
    def __init__(self,pic,bar):
        print(f"[{self.__class__.__name__}] prêt pour le service !")
        self.pic = pic
        self.bar = bar

    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        while len(self.pic.liste_attente)==0: #permets au barman d'attendre 
            await asyncio.sleep(self.pic.tc) 
            if len(self.pic.liste_attente)==0: #si il a attendu un temps de commande et que rien n'est arrivé il peut rentrer chez lui, il n'y a plus de commande
                break
            else:
                while len(self.pic.liste_attente)>=1:
                    c = self.pic.liberer()
                    print(f"[{self.pic.__class__.__name__}] post-it '{c}' libéré")
                    if len(self.pic.liste_attente) == 0:
                        print(self.pic,'\nPic est vide')
                    else: 
                        print(self.pic)
                    print(f'[{self.__class__.__name__}] je commence la fabrication de {c}')
                    await asyncio.sleep(self.bar.tp)
                    logging.info(f'[{self.__class__.__name__}] fonction prepare utilisée au temps {time.time()-t0}')
                    print(f'[{self.__class__.__name__}] je termine la fabrication de {c}')
                    self.bar.recevoir(c)
                    print(f"[{self.bar.__class__.__name__}] '{c}' reçu")
                    print(self.bar)
            

# Fermeture du gestionnaire de journalisation 
logging.shutdown()
