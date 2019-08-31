try:
    file = open("this.text" , 'R')
except EOFError as e:
    print("EOF error")