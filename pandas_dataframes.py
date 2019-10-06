# Pandas dtaframes
import pandas as pd
import numpy as np 

df = pd.DataFrame()
# print(df)  

df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,13,11],[23,24,25,26],[21,22,23,24]],columns=['A','B','C','D'])
# print(df1.head(3))
# print(df1.tail(3))
# print(df1.shape)  
# print(df1.iloc[0,1])
# print(df1.iloc[0:2,0:2])
# print(df1.iloc[0:2,1:3])

print(df1)  