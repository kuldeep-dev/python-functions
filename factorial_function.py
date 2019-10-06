# factorial function

# 3! = 3*2*1
# 2! = 2*1
# 6! = 6*5*4*3*2*1

# 


    

# if __name__ == '__main__':
#     print("Enter the number")
#     number = int(input())
#     factorial = 1

#     if(number<0):
#         print("Error: Factorial of a negative number is not defined") 

#     elif(number==0):
#         print(1)

#     else:
#         for i in range(1,number+1):
#             factorial = factorial*i

#         print("the factorial of" , number,"is",factorial)           

def factorial(number):
    factorial = 1

    if(number<0):
        print("Error: Factorial of a negative number is not defined") 

    elif(number==0):
        print(1)

    else:
        for i in range(1,number+1):
            factorial = factorial*i
        return factorial    


if __name__ == '__main__':      
    print("Enter the number")
    number = int(input())
    print("the factorial of" , number,"is",factorial(number))          