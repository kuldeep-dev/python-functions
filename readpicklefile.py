import pickle

filename = "kuldeep.pkl"
fileObj = open(filename, 'rb')
b = pickle.load(fileObj)

print(b)
