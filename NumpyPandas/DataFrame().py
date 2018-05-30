import  pandas as pd

#https://www.cnblogs.com/chaosimple/p/4153083.html十分钟高低pandas

#米筐
#https://www.ricequant.com/community/topic/3558//6

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    } ,index=[0,1,2,3])
print(df1)

df2=pd.DataFrame({'A':['xy','091','ch','ef'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']},index=[5,6,7,8] )

print('df2: ',df2)


results=pd.concat([df1,df2],axis=0)
print(results)


results1=pd.concat([df1,df2],axis=1)  ###两张表横着放
print(results1)

result2 = pd.concat([df1,df2], keys=['x', 'y'], axis=1)
print(result2)  #两张表横放，但是会以key重新对组成 添加个索引

print(result2['x'])

dates=pd.date_range('20170301',periods=5)
print(dates)





'''
tt ={'aa':[1,2,3],'xy':[2,4,5]}#字典
print(tt)

print(tt['xy'])



使用位置选取数据：
df.iloc[行位置,列位置]
df.iloc[1,1] #选取第二行，第二列的值，返回的为单个值
df.iloc[[0,2],:] #选取第一行及第三行的数据
df.iloc[0:2,:] #选取第一行到第三行（不包含）的数据
df.iloc[:,1] #选取所有记录的第二列的值，返回的为一个Series
df.iloc[1,:] #选取第一行数据，返回的为一个Series
PS：iloc 则为 integer & location 的缩写


'''
