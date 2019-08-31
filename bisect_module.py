# bisect Module

import bisect

number = 33

a = [1,2,31,4,6,7,8,9,34]
# print(a)

print(bisect.bisect(a,number))
bisect.insort(a,number)
print(a)
