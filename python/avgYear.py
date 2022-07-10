
from audioop import avg
import os
#os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np



for state in os.listdir("data/states"):
    avg_list = list()
    
    df = pd.read_csv(f"data/states/{state}/{state}_climate.csv", encoding='utf-8')
    year = df.loc[0]["Date (String)"][:4]
    
    collist = df.columns.tolist()[1:]#피쳐 리스트
    state_df = pd.DataFrame(columns=df.columns.tolist()) #만들 빈 df
    
    avg_year = {}
    for i in range(len(collist)):
        avg_year[collist[i]] = 0 
    print(avg_year)
    day_num = 0
    
    for i in range(len(df)):
        if df.loc[i]["Date (String)"][:4] != year:
            year = df.loc[i]["Date (String)"][:4]
            for j in range(len(collist)):
                avg_year[collist[j]] = avg_year[collist[j]]/day_num
            date_avg_year = {"Date (String)": year}
            date_avg_year.update(avg_year)
            # print(date_avg_year)
            # print("=============")
            # print(df.columns.tolist())
            # print("=============")
            # print(list(date_avg_year.values()))
            date_avg_year=pd.DataFrame([list(date_avg_year.values())], columns=df.columns.tolist())
            print(date_avg_year)
            avg_list.append(date_avg_year)
            
            avg_year = {}
            for i in range(len(collist)):
                avg_year[collist[i]] = 0 
            day_num = 0
            
        for col in collist:
            avg_year[col] += float(df.loc[i][col])
            day_num += 1
    avg_df = pd.concat(avg_list)
    print(avg_df)
    avg_df.to_csv(f"data/climate/{state}/{state}_avg_year.csv", index=False)


'''
목표: 모든 주마다 피쳐별로 평년 평균값들을 만들어야함.

1. 한 주에 접근해서 1년 단위로 각 피쳐를 다 더하고 평균을 구함.
2. 1987~2017년까지 데이터프레임 만듬 
3. 이를 각 주마다 실행.

'''