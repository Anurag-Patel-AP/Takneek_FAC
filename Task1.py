import pandas as pd
rt=pd.Series([0.5,0.7,0.3,-0.4,1.3,0.75,0.83,0.43,-0.23,0.23])
rf=0.3
re=rt.mean()
std=rt.std()
sharpe=(re-rf)/std
print("Sharpe Ratio =",round(sharpe,2))
rtn=pd.Series([-0.4,-0.23])
stdn=rtn.std()
sortino=(re-rf)/stdn
print("Sortino Ratio =",round(sortino,2))