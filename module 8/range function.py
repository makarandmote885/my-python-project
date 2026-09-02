# range function using for loop used to generate sequence of integer in given interval 
# range (start,stop,step) stop is not included 
# syntax  
#  for i in range(start,stop,step)
                #statement 

for i in range(1,12,1):
    print(i)

# even number from 1 to 10
 
for s in range(0,10,2):
    print(s) 

#reverse order 20 to 10

for a in range(20,10,-1):
    print(a)

# range (start,stop) = step is = 1 by default
# range (stop) = start is 0 by default

profits = [23,45,64,34]
for i in range(len(profits)):
   
    print(i+1,profits[i])

       
     