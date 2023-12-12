#!/bin/env python3

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w]*") #Pour trouver un mot

class MRWordFreqCount(MRJob):
    def mapper(self, _, line):
        for word in WORD_RE.findall(line.strip().lower()): 
            yield word.lower(), 1 #renvoie clée , valeur 

    def reducer(self, word, counts):
        yield word, sum(counts) #clée , somme sur valeur avec la bonne clée

class moyenne_sansCombiner(MRJob):
    def mapper(self, _, x):
        yield _, float(x)

    def reducer(self, _, valeurs):
        L_valeurs = list(valeurs)
        yield "Moyenne (sans combiner) : ", f"{sum(L_valeurs)/len(L_valeurs):.3f}"

class moyenne_avecCombiner(MRJob):
    def mapper(self, _, x):
        yield _, float(x)

    def combiner(self, _, valeurs):
        L_valeurs = list(valeurs)
        yield _, sum(L_valeurs)/len(L_valeurs)

    def reducer(self, _, valeurs):
        L_valeurs = list(valeurs)
        yield "Moyenne (avec combiner) : ", f"{sum(L_valeurs)/len(L_valeurs):.3f}"


if __name__ == '__main__':
    #MRWordFreqCount.run()
    moyenne_sansCombiner.run()
    moyenne_avecCombiner.run()
