import os
import requests
import argparse
import numpy as np
import pandas as pd
import json
from numpy.random import default_rng


# Exemple de requête POST

def post_dummy_json(route):
    r = requests.post(os.path.join('http://127.0.0.1:5000/', route),
                      json={'userID': 65, 'value': [1, 2, 3]})
    return r


def post_data_linear_json(route):
    # Ouvrir le fichier JSON en mode lecture
    with open('data_for_prediction.json', 'r') as file:
        json1 = json.load(file)     
    #try
    r = requests.post(os.path.join('http://127.0.0.1:5000/', route),
                      json=json1)
    return r





parser = argparse.ArgumentParser() # lit les arguments dans ligne de commandes 
parser.add_argument('-r', '--route', type=str) #-r rajouter l'argument -r qui lui prend la route 
 
args = parser.parse_args() #récupère l'agument
route = args.route #choppe le string

if 'add-json-value' in route:
    r = post_dummy_json(route)
    print(r.json())

if 'predict' in route:
    r = post_data_linear_json(route)
    print(r.json())