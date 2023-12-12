#!/bin/env python3

import os, time, sys
import multiprocessing
import datetime
import logging
import importlib

path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs'


#Données temporelles
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
m = datetime.datetime.now().minute



# Spécifiez le chemin du dossier que vous souhaitez créer
dossier = "log"

# Utilisez os.makedirs() pour créer le dossier s'il n'existe pas
os.makedirs(dossier, exist_ok=True)

os.makedirs('/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs/Result', exist_ok=True)

#créer un fichier log_temps dans le dossier log 
logging.basicConfig(filename=f'log/jobs_{m}-{d}_{h}-{m}',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class MyProcess(multiprocessing.Process):
  def __init__(self,path):
    multiprocessing.Process.__init__(self)
    self.path = path
    self.path_result = path +'/Result'
    self.list_jobs = [l for l in os.listdir(path) if l.endswith('.py')]


  def run(self):

    binome_path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs/modules'
    sys.path.append(self.path)
    sys.path.append(binome_path)
    t0 = time.time()

    for job in self.list_jobs:
        t1 = time.time()-t0
        logging.info(f"Starting job: {job} au temps {t1}")
        
        # N'utilisez que le nom du module (sans '.py') pour l'importation
        module_name = os.path.splitext(job)[0]
        module = importlib.import_module(module_name)
        result = module.run()
        with open(self.path_result + f'/{module_name}.result','w') as f:
            f.write(str(result))
        logging.info(f"temps d'exécution job: {job} est de  {time.time() - t1}")
            

               
    # Supprimer le chemin ajouté pour éviter des problèmes potentiels
    sys.path.remove(self.path)
    sys.path.remove(binome_path)

    


if __name__ == '__main__':
  myprocess = MyProcess(path)
  myprocess.start()
  myprocess.join()
