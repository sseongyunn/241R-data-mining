#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
from itertools import combinations

###############################################################################
def print_word_freq(filename, word_freq):       #6줄
    #1gram print 함수
    with open( filename, "w", encoding='utf-8') as fin:
        for w, freq in sorted(word_freq.items()):
            print("%s\t"%w, freq, sep='',file=fin)

###############################################################################
def get_coword_freq(filename):                  #32줄
    word_freq = defaultdict(int)
    coword_freq = defaultdict(int)
    word_context_size = defaultdict(int)
        
    with open( filename, "r", encoding='utf-8') as fin:
        
        for line in fin.readlines():
            bigram_list = []
            words = set(line.split())
            #문장 단어들,중복 없어진 set으로 만들기까지 ok, 한 줄만
            
            num = len(words)
            for word in words:
                word_freq[word] += 1
                word_freq["#Total"] += 1
                word_context_size[word] += num
            #set 기준으로 word_freq 딕셔너리에 1gram 정보 넣기 ok
            
            for target, coword in combinations(words, 2):
                if target < coword: #(target, coword) 튜플로 저장
                    bigram_list.append((target, coword))
                else: #(coword, target) 튜플로 저장
                    bigram_list.append((coword, target))
            
            for bigram in bigram_list:
                coword_freq[bigram] += 1
            
    return word_freq, coword_freq, word_context_size

###############################################################################
def print_coword_freq(filename, coword_freq):   #5줄
    with open( filename, "w", encoding='utf-8') as fin:
        for w, freq in sorted(coword_freq.items()):
            a,b = w
            print("%s\t%s\t"%(a,b), freq, sep='',file=fin)

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        
        print( 'processing %s' %input_file, file=sys.stderr)
        
        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos] # ex) "2017.tag.context" -> "2017"
        
        # 1gram, 2gram, 1gram context 빈도를 알아냄
        word_freq, coword_freq, word_context_size = get_coword_freq(input_file)

        # unigram 출력
        print_word_freq(file_stem+".1gram", word_freq)
        
        # bigram(co-word) 출력
        print_coword_freq(file_stem+".2gram", coword_freq)

        # unigram context 출력
        print_word_freq(file_stem+".1gram_context", word_context_size)
