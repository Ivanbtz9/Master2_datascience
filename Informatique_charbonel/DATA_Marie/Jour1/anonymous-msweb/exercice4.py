#! /usr/bin/env python3
from mrjob.job import MRJob
from mrjob.step import MRStep
import re 

WORD_RE = re.compile(r"^V,[\d]+,[\d]+")

class MRWordFreqCount(MRJob):
    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__' :
    MRWordFreqCount.run()