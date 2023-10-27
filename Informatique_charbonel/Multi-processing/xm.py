#!/bin/env python3


import os,sys
import time, datetime
import logging
import importlib
import multiprocessing
import argparse

T0 = time.time()

# Path pour l'exécution
path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs'
binome_path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs/modules'

# Récupérer le nombre de processeurs depuis la ligne de commande

parser = argparse.ArgumentParser(description="Execute jobs using multiprocessing.") #crée un nouvel objet ArgumentParser
parser.add_argument("processors", type=int, help="Number of processors")
args = parser.parse_args() # Cette ligne analyse les arguments fournis dans la ligne de commande en fonction des instructions précédemment définies par l'objet parser


#Données temporelles
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
m = datetime.datetime.now().minute

# Spécifiez le chemin du dossier que vous souhaitez créer
dossier = "log_multiprocessing"

# Utilisez os.makedirs() pour créer le dossier s'il n'existe pas
os.makedirs(dossier, exist_ok=True)

#créer un fichier log_temps dans le dossier log 
logging.basicConfig(filename=f'{dossier}/jobs_{m}-{d}_{h}-{m}',
                    level=logging.DEBUG,
                    format='%(levelname)s - %(message)s')

os.makedirs('/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/jobs/Result_multiprocessing', exist_ok=True)

# Fonction pour exécuter les jobs
def execute_job(job):
    
    sys.path.append(path)
    sys.path.append(binome_path)
    t0 = time.time()

    module_name = os.path.splitext(job)[0]

    try:
        logging.info(f"PID: {os.getpid()} - Starting job: {job} at {t0}")

        module = importlib.import_module(module_name)
        result = module.run()
        with open(path + f'/Result_multiprocessing/{module_name}.result','w') as f:
            f.write(str(result))

        logging.info(f"PID: {os.getpid()} - Execution : {job} is {time.time() - t0}")
    except Exception as e:
        logging.warning(f'Il y a eu une erreur avec le job {module_name}: {e}')    
    
    sys.path.remove(path)
    sys.path.remove(binome_path)

if __name__ == '__main__':
    list_jobs = [l for l in os.listdir(path) if l.endswith('.py')]

    with multiprocessing.Pool(processes=args.processors) as pool:
        pool.map(execute_job, list_jobs)
    
    print(f"Le temps d'exécution total est de {time.time() - T0} secondes")