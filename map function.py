#map() is used when you want to apply the same operation to every item in a list 
# we used with lists
number = [1,2,3,4,5,6,7,8]
sqr = map(lambda x:x*x,number)
print(list(sqr))
