#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math # sqrt

###############################################################################
def read_frequency(filename):

    freqs = dict()
    with open( filename, "r", encoding='utf-8') as fin:
        for line in fin.readlines():
            w, freq = line.split("\t")
            freqs[w] = int(freq)

    return freqs

###############################################################################
def calc_tscore(filename, unigrams, unigram_context, uni_N, cutoff):
    
    t_scores = dict()
    
    with open( filename, "r", encoding='utf-8') as fin:
        
        for line in fin.readlines():
            wordA, wordB, Obs = line.split("\t")
            Obs = int(Obs)
            
            if Obs<cutoff: continue
            
            freqA = unigrams[wordA]
            freqB = unigrams[wordB]
            contextA = unigram_context[wordA]
            contextB = unigram_context[wordB]
            ExpA = contextA * freqB / uni_N
            ExpB = contextB * freqA / uni_N
            
            t_scores[(wordA, wordB)] = (Obs - ExpA) / math.sqrt(Obs)
            t_scores[(wordB, wordA)] = (Obs - ExpB) / math.sqrt(Obs)
     
    return t_scores

###############################################################################
def print_tscore(filename, t_scores):   
    with open( filename, "w", encoding='utf-8') as fin:
        for bigram,score in sorted(t_scores.items()):
            word, coword = bigram
            if (not(coword in word)) and score>0 :
                print("%s\t%s\t%.3f"%(word,coword,score), sep='',file=fin)
        
###############################################################################
if __name__ == "__main__":

    CUTOFF = 5 # 공기빈도가 이 값 이상인 경우만 t점수를 계산
    
    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        
        print( 'processing %s' %input_file, file=sys.stderr)

        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos] # ex) "2017.2gram" -> "2017"
    
        print("\tLoading %s.1gram" %file_stem, file=sys.stderr)
        unigrams = read_frequency(file_stem+".1gram")
        
        print("\tLoading %s.1gram_context" %file_stem, file=sys.stderr)
        unigram_context = read_frequency(file_stem+".1gram_context")
        
        uni_N = unigrams['#Total'] # unigram 빈도 합
        
        t_scores = calc_tscore(input_file, unigrams, unigram_context, uni_N, CUTOFF)
        
        print_tscore(file_stem+".tscore", t_scores)
