import pickle

a = ['kuldeep','chotu','rohan','amit']

filename = "kuldeep.pkl"
fileObj =  open(filename , 'wb')
pickle.dump(a,fileObj)

fileObj.close()
