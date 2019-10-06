# Export CSV data file using pandas and numpy using python

import pandas as pd 

df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,13,11],[23,24,25,26],[21,22,23,24]],columns=['A','B','C','D'])

print(df.head())
# df.to_csv('export.csv')
df.to_csv('export.csv' , index=False)
