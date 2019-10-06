#  json in python

import json

json_data = '{"a":1 , "b":2 , "c":3 , "d":4}'
x= json.loads(json_data)
# print(x)
# print(x['b'])
with open('test.json','w') as f:
    json.dump(x,f)


