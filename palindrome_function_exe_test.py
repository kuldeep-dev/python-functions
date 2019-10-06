# Palindrome Function

#take input
print("Enter your number")
number = input()
number = int(number)
# print(type(number))
temp = number
reverse = 0

while(number>0):
    dig = number%10
    reverse = reverse*10+dig
    number = number//10

# print(reverse)

if temp == reverse:
    print("Number is a palindrome")
else:
    print("Number is a not a palindrome")    


# how to create EXE File in Python

# 1. First intall pip instal pyinstaller 
# pyinstaller --onefile filename



