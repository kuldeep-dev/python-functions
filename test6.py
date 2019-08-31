# Map Function

#map (function_to_apply, lists in input)

def square(n):
        return n**2

h1 = [1,2,3,4,5,7]
sq = []

for item in h1:
        sq.append(item**2)

sq = list(map(square,h1))
print(sq)