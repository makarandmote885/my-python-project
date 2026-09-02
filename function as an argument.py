# allows to pass function one to another fuction 
#greet → refers to the function
#greet() → calls the function immediately

def square(x):
    return x * x
def name(func,number):
    return func(number)
print(name(square,5))           # square is func
                               # number is 5