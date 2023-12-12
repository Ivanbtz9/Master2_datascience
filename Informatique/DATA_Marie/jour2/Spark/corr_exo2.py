#! /usr/bin/env python3

from pyspark.sql import SparkSession

# RDD  = (resilient distributed dataset)

spark  = SparkSession.builder.master("local").appName('Botcazou').getOrCreate()
input_file = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/DATA_Marie/jour2/isd-history.txt'

# Récupérer les données
RDD = spark.sparkContext.textFile(input_file).filter(lambda l : len(l)>0 and l[1] in '0123456789')

# Nombre d'enregistrement
nb_stations = RDD.count()
print("\nNombre d'enregistrement : ",nb_stations)

# Nombre de stations par hémisphère
hem = RDD.map(lambda l : ("Nord",1) if l[57]=='+' else (("Sud",1) if l[57]=="-" else ("NA",1)))
nb_stat_hem = hem.reduceByKey(lambda a,b: a+b).sortByKey().collect()
print("\nNombre de stations par hémisphère :")
for hem,cpt in nb_stat_hem :
    print(f"- {hem}\t{cpt} stations")

# 10 stations qui ont eu la période d'activité la plus grande
activite = RDD.filter(lambda l : len(l)>91)
periode = activite.map(lambda l: (int(l[91:95])-int(l[82:86]),l[13:42])) # Clé = période d'activité, Valeur = nom de la station
compte_periode = periode.sortByKey(False).take(10) # Tri décroissant sur les clés
print("\nStations ayant eu la plus longue période d'activité :")
for cpt,stat in compte_periode :
    print(f"- {stat}\t{cpt} ans d'activité")

# Pays ayant le plus de station
stations_par_pays = RDD.map(lambda l: (l[43:47],1)) # Clé = ID pays, Valeur = 1
nb_par_pays = stations_par_pays.reduceByKey(lambda a,b:a+b).map(lambda t:(t[1],t[0])) # Clé = Nombre de station, Valeur = ID pays
pays_plus_representes = nb_par_pays.sortByKey(False).first() # Tri décroissant sur les clés
print(f"\nPays le plus représenté : {pays_plus_representes[1]}\t{pays_plus_representes[0]} stations")

# Nombre de pays possédant des stations
pays = RDD.map(lambda l: l[43:47]).distinct().filter(lambda p: p.strip()!="")
nb_pays = pays.count()
print(f"\nNombre de pays ayant des stations : {nb_pays}")