#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle

###############################################################################
def learn_lm(filename):  #23줄?
    
    f = open(filename,"r")
    bigrams = {}
    s = True

    while s:
        s = f.readline()
        l = s.split()
        l.insert(0,'<s>')
        l.append('</s>')
        
        for i in l:
            if i != '<s>':
                if key in bigrams:
                    bigrams[key].append(i)
                else:
                    bigrams[key] = [i]
            key=i
            
    f.close()
    return bigrams 
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print( "[Usage] %s in-file out-file(pickle)" %sys.argv[0], file=sys.stderr)
        sys.exit()

    filename = sys.argv[1]
    print("processing %s ..." %filename, file=sys.stderr)
    
    bigrams = learn_lm(filename)

    with open(sys.argv[2],"wb") as fout:
        print("saving %s" %sys.argv[2], file=sys.stderr)
        pickle.dump(bigrams, fout)
