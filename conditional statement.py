# control the execution flow 
# ==, >= ,<= , < ,> !=  

 # if" loop

age = float(input("what is your age: "))

if age >= 18 :
    print("you are adult" ) 



#if else  loop

name = (input("what is your name: "))
if name == "makarand":
    print("this is so much big name")
else:
    print( "name is small")  


# print if a number (int) is odd or even 

num = int(input("enter an integer: "))
if num % 2 == 0:
    print("the number is even ")
else:
    print("the number is odd")    


#if-elif-else 


marks = float(input("enter the marks: "))
if marks >=90:
    print("grade is A")

elif marks >=80 :
    print ("grade is c")   
elif marks >=70 :
    print ("grade is D")
else:
    marks >=6050

    print ("grade is fail")  



# nested if     
 
marks = float(input("enter your marks: "))

if marks >= 60:
    print("you are passed")
    if marks >= 90:
        print("grade is A")
    elif 80 <= marks < 90 :
        print("grade is B")
    elif 70 <= marks < 80 :
        print("grade is C")
    else:
        print("you are fail")
else:
    print("better next time ") 
   


# ternary operator
# we can write a expression in single line 
# syntax :- true expression if condion else false expression 
num = int(input("enter a number: "))
print("even") if num % 2==0 else print("odd")            