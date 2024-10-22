#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

###############################################################################
def word_count(filename):

    word_freq = defaultdict(int)
    #word_freq = dict()
        
    with open( filename, "r", encoding='utf-8') as fin:
        for word in fin.read().split():
            
            word_freq[word] += 1
            
            #if word in word_freq:
            #    word_freq[word] += 1
            #else:
            #    word_freq[word] = 1
    
    return word_freq

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()
        
    i=0
    result={} #dict 생성
    
    for input_file in sys.argv[1:]:

        word_freq = word_count( input_file)  #unigram 상태로 바꾸는 것까진 문제 없음
    
        for w, freq in word_freq.items():
            if not(w in result):
                result[w]=[]
                for j in range(20):
                    result[w].append(0)
            result[w][i] = freq
        i = i+1

    for w, freq in sorted(result.items()):
                print("%s\t"%w, freq, sep='')
        
                