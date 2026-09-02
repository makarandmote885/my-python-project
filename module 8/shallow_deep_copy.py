# it is for mutable datatype which is use in list , dict
# it is module copy 
import copy
l1=[1,2,3,[8,4,5]]
# shallow copy 
l2= copy.copy(l1)
print(l2,id(l2))
print(l1,id(l1)) # both the id of list are different 
#replacement 
l1[0]=10     # it will replace the value present in the list 

l1[3][0] = 20
print(l1) # it will change a internal list of list 
print(l2)

#deep copy 
# it will store the internal  list in different location 

l3=[1,2,3,[1,23,4]]
l4=copy.deepcopy(l3)
l3[3][1]=12
l3[0]=10
print(l3)
print(l4)