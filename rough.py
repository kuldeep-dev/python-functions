from time import time

def func1(a,b):
    # kuldeep
    return a+b

def func2(a,b):
    #test
    num1 = a
    num2 = b
    if(a>b and a != 3):
        pass
    sum([4,3])
    return a+b    
    
if __name__ == "__main__":
    init = time()
    for i in range(0,1000):
        func1(3,5)
        print("Kuldeep time", time() - init)
        init = time()
    for i in range(0,1000):
        func2(3,5)    
        print("code test ", time() - init)