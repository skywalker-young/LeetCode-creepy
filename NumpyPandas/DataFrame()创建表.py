import numpy as np
import pandas as pd


a=lambda x : x+2*x

print(a(2))

b=[1,2,3,4,5]
c=[11,22,33,44,55]
d=[b,c]
print(d)
df2=pd.DataFrame(d,index=['a1','a2'],columns=['open','close','high','low','ave'])
#print(df2)
tmp=['afs','sff']

df2['macd']=tmp

print(df2)

df2=df2[['open','macd','close','low','high','ave']]

print(df2)
