#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle
import math # sqrt

###############################################################################
def cosine_similarity(t_vector, c_vector):
    vectorelements = []
    vectorelements.append(t_vector.values())
    vectorelements.append(c_vector.values())
    
    magnitude = []
    
    for i in range(2):
        for element in vectorelements[i]:
            sumofSquare = 0
            sumofSquare += element*element
        magnitude.append(math.sqrt(sumofSquare))
    
    innerproduct = 0
    
    for keyword in t_vector.keys():
        for coword in c_vector.keys():
            if keyword == coword:
                innerproduct += t_vector[keyword]*c_vector[keyword]
    
    return innerproduct/(magnitude[0]*magnitude[1])

###############################################################################
def most_similar_words(word_vectors, target, topN=10):
    
    result = {}
    
    #대상 공기어 집합 설정
    wordSet = set(word_vectors[target].keys())
    for word in word_vectors[target].keys():
        if word in word_vectors.keys():
            cocoword = set(word_vectors[word].keys())
            wordSet = wordSet.union(cocoword)
        
    for word in wordSet:
        if word in target:
            continue
        if word in word_vectors.keys():
            t = word_vectors[target]
            c = word_vectors[word]
            if cosine_similarity(t,c) > 0.001:
                result[word] = cosine_similarity(t,c)
    
    #집합 공기어들만 코사인 유사도 계산(0.001보다 크면 딕셔너리 저장)

    return sorted(result.items(), key=lambda x: x[1], reverse=True)[:topN]

###############################################################################
def print_words(words):
    for word, score in words:
        print("%s\t%.3f" %(word, score))
    
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file(pickle)", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1],"rb") as fin:
        word_vectors = pickle.load(fin)

    while True:

        print('\n검색할 단어를 입력하세요(type "^D" to exit): ', file=sys.stderr)
    
        try:
            query = input()
            
        except EOFError:
            print('프로그램을 종료합니다.', file=sys.stderr)
            break
    
        # result : list of tuples, sorted by cosine similarity
        result = most_similar_words(word_vectors, query, topN=30)
        
        if result:
            print_words(result)
        else:
            print('\n결과가 없습니다.')
