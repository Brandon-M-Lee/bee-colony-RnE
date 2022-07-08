import os
#os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np

def rms(x):
    return np.sqrt(x)

all_n = {
    "평년 최고 기온": 0,
    "평년 최저 기온": 0,
    "평년 최고 이슬점": 0,
    "평년 최저 이슬점": 0,
    "평년 최고 풍속": 0,
    "평년 최저 풍속": 0,
    "평년 강수량": 0,
    "평년 최고 기압": 0,
    "평년 최저 기압": 0
}
useful_n = {
    "평년 최고 기온": 0,
    "평년 최저 기온": 0,
    "평년 최고 이슬점": 0,
    "평년 최저 이슬점": 0,
    "평년 최고 풍속": 0,
    "평년 최저 풍속": 0,
    "평년 강수량": 0,
    "평년 최고 기압": 0,
    "평년 최저 기압": 0
}
all_feature_rms = {
    "평년 최고 기온": 0,
    "평년 최저 기온": 0,
    "평년 최고 이슬점": 0,
    "평년 최저 이슬점": 0,
    "평년 최고 풍속": 0,
    "평년 최저 풍속": 0,
    "평년 강수량": 0,
    "평년 최고 기압": 0,
    "평년 최저 기압": 0
}
useful_feature_rms = {
    "평년 최고 기온": 0,
    "평년 최저 기온": 0,
    "평년 최고 이슬점": 0,
    "평년 최저 이슬점": 0,
    "평년 최고 풍속": 0,
    "평년 최저 풍속": 0,
    "평년 강수량": 0,
    "평년 최고 기압": 0,
    "평년 최저 기압": 0
}
for state in os.listdir('data/states'):
    texts = list()
    corr_ = ""
    print(state)
    try:
        with open(f'data/correlation/{state}.txt', 'r', encoding='utf-8') as f:
            string = f.readlines()
            
            for i in string:
                if i.find("상관 관계") != -1: #첫번째 줄 넘기기
                    continue
                if i.find('상관계수') != -1 or i.find('tau') != -1:
                    texts.append(i)
                    corr_ = i.split()[0]
                    continue
                temp = i.split()
                if corr_ == "pearson": #피어슨만 RMS 계산
                    all_feature_rms[i[ : i.index(":")]] += float(temp[-1])**2
                    all_n[i[ : i.index(":")]] += 1
                try:
                    if abs(float(temp[-1])) > 0.7:
                        texts.append(i)
                        if corr_ == "pearson": #피어슨만 RMS 계산
                            useful_feature_rms[i[ : i.index(":")]] += float(temp[-1])**2
                            useful_n[i[ : i.index(":")]] += 1
                except:
                    pass
        with open('data/correlation/upper 0.7/' + state + '.txt', 'w', encoding='utf-8') as f:
            for i in texts:
                f.write(i)
    except:
        print(f'{state} is NOT found')
        
with open('data/correlation/useful data/useful_feature_rms.txt', 'w', encoding='utf-8') as f:
    f.write("pearson useful feature rms\n")
    for i in useful_feature_rms:
        f.write(f'{i} : {rms(useful_feature_rms[i]/useful_n[i])}\n')
        
    f.write('pearson all feature rms\n')
    for i in all_feature_rms:
        f.write(f'{i} : {rms(all_feature_rms[i]/all_n[i])}\n')