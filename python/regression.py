import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

def process(state):
    df = pd.read_csv(f'data/states/{state}/{state}_avg_year.csv') #학습 데이터
    del df["Date (String)"]
    train_data_np = df.to_numpy()

    df = pd.read_csv(f'data/states/{state}/{state}_bee.csv') #테스트 데이터
    target_data_np = np.array(list(reversed(list(df[" Value"]))))

    train_input, test_input, train_target, test_target = train_test_split(#데이터 분리
        train_data_np, target_data_np, test_size=0.3)
    
    poly = PolynomialFeatures(degree=2) #변수 수를 증가시키는 함수
    poly.fit(train_input)
    train_poly = poly.transform(train_input)
    print(train_poly.shape)
    test_poly = poly.transform(test_input)

    ss = StandardScaler() #데이터 정규화
    ss.fit(train_poly)
    train_scaled = ss.transform(train_poly)
    test_scaled = ss.transform(test_poly)

    return train_scaled, test_scaled, train_target, test_target

def ridgeRegression(state, train_scaled, test_scaled, train_target, test_target):
    ridge = Ridge() #릿지 회귀
    ridge.fit(train_scaled, train_target)
    print(ridge.score(test_scaled, test_target)) #R^2값 확인

    train_score = list()#그래프 그리기 위한 리스트
    test_score = list()
    alpha_list = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    for alpha in alpha_list:
        ridge = Ridge(alpha=alpha)
        ridge.fit(train_scaled, train_target)
        train_score.append(ridge.score(train_scaled, train_target))
        test_score.append(ridge.score(test_scaled, test_target))
    # plt.title(f"{state} with ridge Regression")
    # plt.plot(np.log10(alpha_list), train_score, label="Train")
    # plt.plot(np.log10(alpha_list), test_score, label="Test")
    # plt.xlabel("Alpha")
    # plt.ylabel("R^2")
    # plt.show()

def lassoRegression(state, train_scaled, test_scaled, train_target, test_target):
    lasso = Lasso() #라소 회귀
    lasso.fit(train_scaled, train_target)
    print(lasso.score(test_scaled, test_target)) #R^2값 확인

    train_score = list()#그래프 그리기 위한 리스트
    test_score = list()
    alpha_list = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    for alpha in alpha_list:
        lasso = Lasso(alpha=alpha)
        lasso.fit(train_scaled, train_target)
        train_score.append(lasso.score(train_scaled, train_target))
        test_score.append(lasso.score(test_scaled, test_target))
    # plt.title(f"{state} with Lasso Regression")
    # plt.plot(np.log10(alpha_list), train_score, label="Train")
    # plt.plot(np.log10(alpha_list), test_score, label="Test")
    # plt.xlabel("Alpha")
    # plt.ylabel("R^2")
    # plt.show()
train_scaled, test_scaled, train_target, test_target = process("ALABAMA")
ridgeRegression("ALABAMA", train_scaled, test_scaled, train_target, test_target)
lassoRegression("ALABAMA", train_scaled, test_scaled, train_target, test_target)