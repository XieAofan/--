import pandas as pd
import time

def get_data():
    return pd.read_csv("D:\\32\\Tool\\队值\\花名册.CSV")

def get_people(index = 0):
    df = get_data()
    n = 0
    xl = df['姓名']

    while True:
        
        for i in xl:
            if n >= index:
                yield i
            n = n+1

gt = get_people(37-1)
Z = []
for i in range(8):
    D = []
    n = 3
    n = int(input())
    for j in range(7):
        P = []
        
        for i in range(n):
            P.append(next(gt))
        print('、'.join(P))
        D.append('、'.join(P))
    Z.append(D)
'''      
for i in range(7):
    for j in range(7):
        print(Z[i][j])
time.sleep(10)

''' 

