#!/bin/env python3

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import time

path_data = "~/Bureau/Master_data_science/DATAS_M2/Informatique_charbonel_Marie/DATA_Marie/Projet_Map_Reduce/soc-Epinions1.txt"


class PageRank(MRJob):
    N = 0
    C = 0.15

    def mapper1(self, _, line):
        l = line.split('\t')
        yield l[0], l[1]

    def reducer1(self,page_i,list1):
        filles = []
        ni= 0
        for k in list1:
            filles.append(k)
            ni+=1
        yield None, (page_i,ni,filles)
    
    def reducer2(self,_,list1):
        nb = 0
        L = []
        for k in list1:
            nb+=1
            yield k[0], (k[1], k[2])
        PageRank.N = nb

    def mapper3(self,page_i , line):
        yield page_i, (line[0],1/PageRank.N,line[1])
    
    def mapperT(self,page_i , line):
        yield page_i, line
        for enf in line[2]:
            yield enf , (1-PageRank.C)*(float(line[1])/float(line[0]))

    def reducerT(self,pagei,list2):
        L = []
        W = 0
        for e in list2:
            if isinstance(e,list):
                L = e
            else: 
                W+=e
        W = PageRank.C/PageRank.N +W
        if len(L)==0:
            yield pagei , (0,W,[])
        else:   
            yield pagei , (L[0],W,L[2])
    
    def mapper4(self,page_i,line):
        yield None ,(line[1],page_i)
    
    def reducer4(self, _, list1):
        sorted_results = sorted(list1,reverse=False)
        for result in sorted_results:
            yield  f'{result[0]} est le PageRank de La page: ', result[1]
        
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper1,reducer=self.reducer1),
            MRStep(reducer=self.reducer2),
            MRStep(mapper=self.mapper3),
            *[MRStep(mapper=self.mapperT,reducer=self.reducerT) for i in range(10)],
            MRStep(mapper=self.mapper4,reducer=self.reducer4)]#* spread l'arret
            

if __name__ == '__main__':
    t0 = time.time()
    PageRank1 = PageRank()
    PageRank1.run()
    print(f"Temps d'exécutiondu programme :  {time.time()-t0} secondes")

