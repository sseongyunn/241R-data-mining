#python 최신 버전으로 업데이트(3.12.2)
#numpy 설치(1.26.4)                     | pip install numpy==1.26.4
#pyproject-toml 설치                    | pip install pyproject-toml
#konlpy 설치                            | pip3 install konlpy
# https://yeoeun-ji.tistory.com/65 참고

#품사와 함께 반환
#print(kkma.pos('안녕. 나는 하늘색과 딸기를 좋아해'))
#>> [('안녕', 'NNG'), ('.', 'SF'), ('나', 'NP'), ('는', 'JX'), ('하늘색', 'NNG'), ('과', 'JC'), ('딸기', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('어', 'ECS')]


from konlpy.tag import Kkma
kkma=Kkma()
print(kkma.morphs('안녕. 나는 하늘색과 딸기를 좋아해'))
