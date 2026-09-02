import random
print("welcome to the game ")
while True:
    choice = input("press 'enter' to roll a dice or 'q' to quit")
    choice=choice.strip()
    if choice == 'q':
        print("thanks for playing the game")
        break
    elif choice=='':
        number = random.randint(1 ,6)
        print(f"your number is {number}")
    else:
        print("invalid input")    


