from mrjob.job import MRJob 
from mrjob.step import MRStep
import re

motif = re.compile("\w{5,}")

class MRWordFreqCount(MRJob):
    def mapper(self, _, line):
        #yield _,line
        for word in motif.findall(line):
            yield word.lower(), 1

    def reducer1(self, word, counts):
        yield None, (sum(counts), word)

    def reducer2(self, _, reduc1):
        count,word = max(reduc1)
        #yield _,list(reduc1)
        yield word, count

    def steps(self):
        return [
           MRStep(mapper=self.mapper,
                  reducer=self.reducer1),
          MRStep(reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MRWordFreqCount.run()