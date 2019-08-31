# List comprehension
# Dictionary comprehension
# Set comprehension
# Genrator comprehension


# List comprehension
list_1 = [1,2,3,4,5,6,7,8,123,456,34]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)

print('Without using list comprehension',divide_by_3)        
print('Using list comprehension',[item for item in list_1 if item%3 == 0])        


# Dictionary comprehension
dict_1 = { 'a':45 , 'b':65 , 'A':5}
print({ k.lower():dict_1.get(k.lower(),0) + dict_1.get(k.upper(), 0 ) for k in dict_1.keys()})


# Set comprehension

squared = { x**2 for x in [1,2,3,4,5,3,4,44,44,55,3,44]}
print(squared)

# Genrator comprehension

gen = (i for i in range(56) if i%3 == 0)
# print(gen)
for item in gen:
    print(item)