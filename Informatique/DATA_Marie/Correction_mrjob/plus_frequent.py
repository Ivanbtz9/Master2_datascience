#!/bin/env python3

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]*") #Pour trouver un mot

class MotPlusFreq5(MRJob):
    def mapper1(self, _, line):
        for word in WORD_RE.findall(line.strip().lower()):
            if len(word.lower())>=5:
                yield word.lower(), 1 #renvoie clée , valeur 

    def combiner1(self, word, valeurs):
        L_valeurs = list(valeurs)
        yield word, sum(L_valeurs)

    def reducer1(self,word,count):
        yield None, (sum(count), word)
    
    def mapper2(self,_,tup):
        yield None, tup 

    def reducer2(self,_,X):
        count,word = max(X)
        yield word, count

    def steps(self):
        return [MRStep(mapper=self.mapper1,combiner=self.combiner1,reducer=self.reducer1),
        MRStep(mapper=self.mapper2,reducer=self.reducer2)
        ]
    
if __name__ == '__main__':
    MotPlusFreq5.run()

