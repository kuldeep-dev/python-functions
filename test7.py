def greater_then_2(n):
        if n>2:
                return True
        else:
                return False

h1 = [1,2,3,4,5,6,7,-3,-4]
greater_then_2 = list(filter(greater_then_2 , h1))
print(greater_then_2)        