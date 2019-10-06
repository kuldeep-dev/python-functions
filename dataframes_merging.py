#  Dataframes Merging

import pandas as pd

df1 = pd.DataFrame([[1,2,3],[2,7,3],[6,3,9]],columns=['A','B','C'])
# print(df1)
df2 = pd.DataFrame([[11,12,123],[22,47,35],[63,32,92]],columns=['X','Y','Z'])
# print(df2)

df3 = pd.merge(df1,df2, right_on='Y',left_on='B')
print(df3)


