#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle
import random # choice

def generate_sentence(bigrams, start_with = '<s>'):

    key = start_with
    if key == '<s>':
        sentenceL = []
    else:
        sentenceL = [key]
    
    while key != '</s>':
        list = bigrams.get(key,[])
        if list != []:
            next = random.choice(list)
            if next != '</s>':
                sentenceL.append(next)
        else:
            next = '</s>'    
        key = next
        
    # if key == '<s>': sen = random.choice(bigrams.get('<s>'))
    # else: sen = key
    # i = 0
    
    # while 1:
    #     l=sen.split()
    #     add = random.choice(bigrams.get(l[i]))
    #     if add == '</s>': break
    #     sen = sen + ' ' + add
    #     i = i+1
    
    # print(sen)
    
    sentence = ' '.join(sentenceL)
    print(sentence)
    
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage] %s in-file(pickle)" %sys.argv[0], file=sys.stderr)
        sys.exit()

    with open(sys.argv[1],"rb") as fp:
        bigrams = pickle.load(fp)

    for i in range(10):
        print(i, end=' : ')
        generate_sentence(bigrams, "나는")
        print()
