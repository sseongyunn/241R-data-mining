#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf

###############################################################################
# 색인어 (명사, 복합명사 등) 추출, 원래 23줄

# 색인 대상 형태소 : NNG(일반명사), NNP(고유명사), NR(수사), NNB(의존명사), SL(외국어;영어), SH(한자), SN(숫자)
# 색인어 해당 품사가 여러 번 이어지는 복합어의 경우 복합어를 구성하는 단일어를 모두 출력한 뒤 복합어 출력
# 셋 이상의 단일어가 연속되는 경우 가장 긴 복합어만 출력
# NNG, NNP, SH, SL은 단일어로도 색인어 추출
# 단, SL이 복합어에 속하는 경우 단일어로는 색인어로 추출하지 않음 ex. SK텔레콤
# NR, NNB, SN은 단일어로는 색인어로 추출하지 않음
# 입력 리스트는 튜플의 리스트

# monolingual 리스트와 non_monolingual 리스트 구성
# mono false
# 단어 받기
# monolingual일 때         if: SL이면 complex에만 추가
#                         else: nouns에 추가, complex에 추가, mono true
# 
# non_monolingual일 때     complex에 추가
# 
# 둘 다 아닐 때              if, complex의 요소 개수가 2개 이상이고, mono true: complex 한 번에 nouns에 추가, complex 리스트 reset
#                         else, SL하나만 들어와있거나, 다른 monolingual 하나만 들어와있거나 쌓인 monolingual이 없이 비색인어가 연속으로 들어온 경우: complex 리스트 reset, mono false로 만들기

def get_index_terms(mt_list):
    nouns = []
    
    monolingual = ['NNG', 'NNP', 'SH', 'SL']
    non_monolingual = ['NR', 'NNB','SN']
    complex=[]
    mono = False
    SL = False
    end = len(mt_list)
    k=0
    
    for i in mt_list:
        word=i[0]
        tag=i[1]
        k=k+1
        if tag in monolingual:
            if tag == 'SL':
                complex.append(word)
                SL = True
            else:
                nouns.append(word)
                complex.append(word)
                mono = True
        elif tag in non_monolingual:
            complex.append(word)
        else:
            if len(complex)>1:
                complexWord = ''.join(complex)
                nouns.append(complexWord)
                complex =[]
                mono = False
                SL = False
            elif len(complex)==1 and SL == True:
                complexWord = ''.join(complex) #그냥 넣을 수 있는 방법 없나?
                nouns.append(complexWord)
                complex=[]
                SL=False
            else:
                complex =[]
                mono = False
        if k==end and (len(complex)>1 or (len(complex)==1 and SL==True)):
            complexWord = ''.join(complex)
            nouns.append(complexWord)

    return nouns

###############################################################################
# Converting POS tagged corpus to a context file
def tagged2context( input_file, output_file):
    try:
        fin = open( input_file, "r", encoding='utf-8')
    except:
        print( "File open error: ", input_file, file=sys.stderr)
        sys.exit()

    try:
        fout = open( output_file, "w", encoding='utf-8')
    except:
        print( "File open error: ", output_file, file=sys.stderr)
        sys.exit()

    for line in fin.readlines():

        # 빈 라인 (문장 경계) \n: 줄바꿈
        if line[0] == '\n':
            print("", file=fout)
            continue

        try:
            ej, tagged = line.split(sep='\t')
        except:
            print(line, file=sys.stderr)
            continue

        # 형태소, 품사 추출
        # result : list of tuples
        result = mf.get_morphs_tags(tagged.rstrip())

        # 색인어 추출
        terms = get_index_terms(result)

        # 색인어 출력
        for term in terms:
            print(term, end=" ", file=fout)

    fin.close()
    fout.close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        output_file = input_file + ".context"
        print( 'processing %s -> %s' %(input_file, output_file), file=sys.stderr)

        # 형태소 분석 파일 -> 문맥 파일
        tagged2context( input_file, output_file)
