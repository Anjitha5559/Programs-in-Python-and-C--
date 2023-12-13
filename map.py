# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
from functools import reduce

nums = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n+2 ,evens))
summ = reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(summ)