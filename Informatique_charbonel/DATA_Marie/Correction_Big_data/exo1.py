#!/bin/env python3

path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/DATA_Marie/Jour1/stop_areas.json'

import json

from pprint import pprint

with open(path,'r') as f:
    data=json.load(f)

#pprint(data) # Print formaté

print(type(data)) # <class 'dict'>
print(type(data['stop_areas'])) # <class 'list'>
print(data['stop_areas'][0].keys()) # <class 'dict'>
print(data['stop_areas'][0]['coord']) 

import pandas as pd
df = pd.DataFrame(columns=["nomGare","latitude","longitude"]) # création d'un dataframe vide à 3 colonnes

for gare in data['stop_areas'] :
    L =[ gare['name'], gare["coord"]["lat"],gare["coord"]["lon"]]

    nouvelle_ligne = dict(zip(df.columns,L))

    df = df._append(nouvelle_ligne, ignore_index=True) # ajoute une ligne au dataframe

pprint(df)

df.to_csv("ex1_out.csv", index=False)
print("Création du fichier : ex1_out.csv")