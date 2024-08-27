import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data=yf.download("AAPL",'2023-01-01', '2024-01-01')

data['ema12'] = data['Close'].ewm(span=12, adjust=False, min_periods=12).mean()

data['ema26'] = data['Close'].ewm(span=26, adjust=False, min_periods=26).mean()

data['MACD']=data['ema12']-data['ema26']

data['signals'] = data['MACD'].ewm(span=9, adjust=False, min_periods=9).mean()

signal=[]
for l in range(len(data)):
    if data['MACD'].iloc[l-1]<data['signals'].iloc[l-1] and  data['MACD'].iloc[l]>data['signals'].iloc[l]:
        signal.append(1)
    elif data['MACD'].iloc[l-1]>data['signals'].iloc[l-1] and  data['MACD'].iloc[l]<data['signals'].iloc[l]:
        signal.append(-1)
    else:
        signal.append(0)
        pass


data['Signal']=signal 

signal_1 = 0
signal_2 = 0
for i in range (len(data)):
    if data['Signal'].iloc[i]==1:
            signal_1 += 1
    elif data['Signal'].iloc[i]==-1:
            signal_2 += 1 
    else:
         pass

print('no. of 1 :', signal_1)
print('no. of -1 :', signal_2)

print(data)