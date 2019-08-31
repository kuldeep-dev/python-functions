# Iterable -- 
# Iterator
# Iteration

def gen(n):
    for i in range(n):
        yield i


# for i in gen(1000):
    # print(i)

# print(gen(1000))

# for i  in gen(1000):
    # print(i)

obj =  gen(1000)
print(next(obj))
print(next(obj))    