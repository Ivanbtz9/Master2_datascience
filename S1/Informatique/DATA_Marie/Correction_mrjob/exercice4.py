#!/bin/env python3

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

path_data = '/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/DATA_Marie/jour2/anonymous-msweb.data'



WORD_RE = re.compile(r"[\w]*") #Pour trouver un mot

class Question1(MRJob):
    def mapper(self, _, line):
        line_split = line.split(',')
        if line_split[0]=='V' :
            yield line_split[1], 1

    def combiner(self,id,visite):
        NbVisites = sum(list(visite))
        yield id, NbVisites

    def reducer(self, id, visite):
        NbVisites = sum(visite)
        if NbVisites >= 1000 :
            yield id, f"{NbVisites} visites"

class Question2(MRJob):
    def mapper(self, _, line):
        line_split = line.split(',')
        if line_split[0]=='V' :
            yield line_split[2], 1

    def combiner(self,id,visite):
        NbVisites = sum(list(visite))
        yield id, NbVisites

    def reducer(self, id, visite):
        NbVisites = sum(visite)
        if NbVisites >= 1000 :
            yield id, f"{NbVisites} visites"
    
if __name__ == '__main__':
    Question2.run()

