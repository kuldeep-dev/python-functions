# *args and **kwargs tutu

def function_1 (*args):
  #print(type(args))
  #print(len(args))
  if(len(args) == 3):
    print("the name is",args[0] , "and the age is " , args[1] , "and the roll no is" , args[2])
  else:
    print("the name is",args[0] , "and the age is " , args[1])

lis = ["kuldeep",32 , 234] 

#function_1(*lis)

def printmarks(**kwargs):
    print(type(kwargs))
    for key , value in kwargs.items():
      print(key,value)


marlistdata = {"kuldeep" : 100 , "rohan" : 30 , "amit" : 58}

#printmarks(**marlistdata)

def master(normal , *arks , **kwarks):
  print(normal)
  for i in arks:
    print(i)
  for key , value in kwarks.items():
      print(key,value)   


master("normal" , lis , marlistdata)      