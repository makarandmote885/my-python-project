import random
#random()-return random float between 1.0 and 2.0
print(random.random())   # generate a decimal number 0 to 1 
print(random.randint(0,2))   #Generates a random integer between two numbers including both ends.
print(random.randrange(0,2))
names=["makarand","apeksha","manu"] 
print(random.choice(names))   #choice = pick one 🎯
numbers = [1,2,3,4,5,6]
random.shuffle(numbers)    #shuffle = mix the whole list 🔀
print(numbers)
numbers = [1, 2, 3, 4, 5]
result = random.sample(numbers, 3)
print(result)


# game 
import random

number = random.randint(1, 10)

guess = int(input("Guess the number: "))

if guess == number:
    print("Correct! 🎉")
else:
    print("Wrong!")
    print("The number was:", number)