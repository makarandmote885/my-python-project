student = {"maths": 10, "phy": 20, "chem": 40}
print(student.get("phy"))
# get is use for to get the value of key
# if we want to give a default value for key is not present in dict
print(student.get("bio", 50))


# membership operator => in
print("maths" in student)  # its look for key only not value

# update is use to update
shop1 = {"milk": 20, "rice": 30, "chiken": 100}
shop2 = {"milk": 30, "dal": 40, "salt": 40}
shop1.update(shop2)
print(shop1)


# pop() to delete the key value pair
shop1.pop("milk")
print(shop1)

# keys cannot be duplicate in a dict
# its read from right to left

# keys cannot be list[] ,sets{},dict they are mutable
# allowed keys string,intger,float,bool,tuples() they are immutable
# values can be any datatypes

# fetch the keys
print(shop1.keys())
print(shop1.values())
print(shop1.items())  # which store in tuple or which show in tuples
