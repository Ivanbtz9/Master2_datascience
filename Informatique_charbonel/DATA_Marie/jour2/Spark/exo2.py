from pyspark import SparkContext
import sys
import re

sc = SparkContext()

path = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/DATA_Marie/jour2/isd-history.txt'

lines = sc.textFile(path)

###Question 1
filter_lines = lines.filter(lambda line: len(line)>0 and line[1].isdigit())

"""print(filter_lines.collect())"""

###Question 2

# Compter le nombre d'enregistrements
count = filter_lines.count()

# Afficher le nombre d'enregistrements

"""print("Nombre d'enregistrements:", count)"""

####Question 3


# Filtrer les lignes en fonction de la latitude
def lat(signe):
    if signe =='+':
        return "Nord"
    elif signe =='-':
        return "Sud"
    else:
        return "NA"

# Appliquer la fonction de filtrage et compter les stations dans chaque hémisphère
RDD_lat = filter_lines.map(lambda l : (lat(l[57]),1))

"""print(RDD_lat.take(10)) #pour en prendre 10"""

RDD3 = RDD_lat.reduceByKey(lambda a,b:a+b)

#print(RDD3.collect())
"""
print("Nombre de stations par hémisphère :")
for hemisphere, count in RDD3.collect():
    print(f"- {hemisphere}\t{count} stations")"""

####Question 4

# Filtrer les lignes pour exclure celles où la date de fin n'est pas renseignée
filtered_date = lines.filter(lambda line: len(line) >= 98)
print(f'il y a {filtered_date.count()} stations avec des dates')

# Mapper pour extraire l'ID de la station et calculer la période d'activité
def extract_station_id_and_activity_period(line):
    station_id = line[0:6].strip()
    begin_date = line[81:89]
    end_date = line[90:98]
    activity_period = (station_id, int(end_date) - int(begin_date))
    return activity_period


# Appliquer le mappage
activity_periods = filtered_date.map(extract_station_id_and_activity_period) # ou bien (lambda line : extract_station_id_and_activity_period(line))
#print(activity_periods.collect())

# Trier les stations par période d'activité décroissante
sorted_stations = activity_periods.sortBy(lambda x: x[1], ascending=False)

# Prendre les dix premières stations
top_10_stations = sorted_stations.take(10)

# Afficher les résultats
"""print("Les dix stations avec la plus longue période d'activité :")
for station in top_10_stations:
    station_id, period = station
    print(f"Station {station_id} - Période d'activité : {period} jours")"""



