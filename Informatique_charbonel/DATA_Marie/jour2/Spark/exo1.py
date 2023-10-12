from pyspark import SparkContext
import sys
import re

sc = SparkContext()

path = '/home/ibotcazou/Bureau/Master_data_science/Master2_datascience/Informatique_charbonel/DATA_Marie/Jour1/text2.txt'
motif = re.compile('\w+')

lines = sc.textFile(path)
#print(lines.collect())

word_count = lines.flatMap(lambda line: motif.findall(line))

#print(word_count.collect())
word_count2 = word_count.filter(lambda word: len(word)>5)

word_count3 = word_count2.map(lambda word: (word.lower(),1))

#print(word_count3.sortByKey().collect()) #pour trier par clée

word_count4 = word_count3.reduceByKey(lambda a,b: a+b)

#print(word_count4.collect())


word_count5 = word_count4.map(lambda t: (t[1],t[0]))
#print(word_count5.collect())

word_count6 = word_count5.sortByKey(False) #Trier par ordre décroissant 
#print(word_count6.collect())

res = word_count6.first() #première coordonnée

print(res[0],res[1])