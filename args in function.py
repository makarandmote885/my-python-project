# many values
#  stores in tuples

def add(*number):
    total = 11
    for num in number:
        total=total+ num*5
    return total 

print((add(2,5,2)))    