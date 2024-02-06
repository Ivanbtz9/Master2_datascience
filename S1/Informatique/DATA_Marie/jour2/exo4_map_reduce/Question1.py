from mrjob.job import MRJob 
from mrjob.step import MRStep
import re

#Afficher les ID et le nombre de visites des pages qui ont été visitées plus de 600 fois.



class MRWordFreqCount(MRJob):
    def mapper(self, _, line):
        yield _,line
        #for word in motif.findall(line):
            #yield word.lower(), 1

    def steps(self):
        return [
           MRStep(mapper=self.mapper)
        ]

if __name__ == '__main__':
    MRWordFreqCount.run()