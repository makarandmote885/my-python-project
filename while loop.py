# depend on condition A while loop repeats the code as long as a condition is true. 
# it will run till the statement is true after false it will come back 
#syntax   
"""
while condition :
    statement
"""

num=1
while num < 10:
    print(num)
    num = num +2

#infinite while  loop
correct_password = "12345678"
while True:
    user_password=input("enter your password: ")
    if user_password==correct_password:
        print("password is correct")
        break
    else:
        print("wrong password ")

