# keep the items which  you want (selected item )
number=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x: x % 2 == 0,number))
print(result)


# reduce() function
#combines items and get one value 
from functools import reduce
number = [323,2,2,3,2,23,2,]
result = reduce(lambda a,b: a+b , number)
print(result)