
import os
#os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np
for state in os.listdir("data/states"):
    df = pd.read_csv(f"data/states/{state}/{state}_climate.csv", encoding='utf-8')
    year = df.loc[0]["Date (String)"][:4]
    avg_year = {}
    collist = df.columns.tolist()[1:]
    state_df = pd.DataFrame(columns=collist)
    
    

    for i in range(len(collist)):
        avg_year[collist[i]] = 0 
    print(avg_year)
    for i in range(len(df)):
        if df.loc[i]["Date (String)"][:4] != year:
            year = df.loc[i]["Date (String)"][:4]
            state_df = 
            
        for col in collist:
            avg_year[col] += float(df.loc[i][col])
    print(state_df)
    break


'''
목표: 모든 주마다 피쳐별로 평년 평균값들을 만들어야함.

1. 한 주에 접근해서 1년 단위로 각 피쳐를 다 더하고 평균을 구함.
2. 1987~2017년까지 데이터프레임 만듬 
3. 이를 각 주마다 실행.

'''