# for loop we know the fix iteration of program 
# A for loop is used when you want to repeat something for a known number of times or go through
#  items in a collection such as a list. 
"""
 it is an iterator based loop which step through the items of a collection 
 (lists,tuples,sets,dict,str) and execute a block of code repeatedly for a
 number of times equal to the items /elements of that collection
 """

percent = [85,67.89,56,47]
for p in percent:
    print(p)


# for loop string
s1 = "hello world"
for char in s1:
    print(char)     #it prints one by one 

#for loop in dict
employee = {'empid':12 ,'name':"makarand",'department':"hr"}
for i in employee:
    print(i)   # it will print only keys
    print(i,employee[i]) # it will print whole dict

    print(employee.items())
    for s in employee.items():
        print(s)
