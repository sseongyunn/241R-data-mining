#!/usr/bin/env python3
# coding: utf-8

import sys

###############################################################################
# 형태소 분석 결과로부터 형태소와 품사들을 알아냄
# return value : (형태소, 품사)로 구성된 tuple들의 list
# 주의할 점: 어절 내 +나 /가 있을 때 처리
# “공동정권	“/SS+공동정권/NNG
# SK텔레콤+신세기통신	SK/SL+텔레콤/NNG++/SW+신세기통신/NNP
# [CF히트예감]한국통신엠닷컴/결정적	[/SS+CF/SL+히트/NNG+예감/NNG+]/SS+한국통신엠닷컴/NNP+//SP+결정적/NNG

# 형태소 추출
# ch가 /이기 전까지 morphsList에 집어넣기
# 만약 list에 아무것도 없는데 /인 경우 list에 / 집어넣기
# -> if ch != '/' or morphsList==[]
# /가 나오면 품사추출진행

#품사 추출
# ch가 +가 나오기 전까지 tagsList에 집어넣기
# +가 나오면
# 튜플로 만들어 result 리스트에 넣기
# morphsList와 tagsList 리셋

def get_morphs_tags(tagged):

    result = []
    morphsList = []
    tagsList = []                         # morphsList와 tagsList 리셋
    morphTurn = True                      #형태소 추출 차례인지 품사 추출 차례인지 구분하기 위해
    end = len(tagged)                     #맨 마지막 형태소,품사 튜플이 result에 안 들어가고 반복문 종료되는 문제 해결용
    i = 0
    
    for ch in tagged:
        i = i+1
        if morphTurn==True:
            if ch != '/' or (ch =='/'and morphsList == []):
                morphsList.append(ch)
            else:
                morphResult = ''.join(morphsList)
                morphsList=[]
                morphTurn=False
        else:
            if ch != '+':
                tagsList.append(ch)
                if i == end: 
                    tagResult = ''.join(tagsList)
                    result.append((morphResult, tagResult))
            else:
                tagResult = ''.join(tagsList)
                tagsList = []
                result.append((morphResult, tagResult))
                morphTurn=True

    return result

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], encoding='utf-8') as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2:
                continue

            # result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())

            for morph, tag in result:
                print(morph, tag, sep='\t')