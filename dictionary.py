# comma seperated key value pair enclosed within {}
# {key1:value1 , key2:value2}
items = {"milk": 60, "rice": 40, "colgate": 50}
print(items, type(items))  # in python it is called as dict
print(len(items))

print(items["milk"])
# it is mutable we can change the value of key
# how to change the value
items["milk"] = 70
print(items)
# add new key value pair
items["egg"] = 40
print(items)
# practice
marks = {"apeksha": 99, "makarand": 98}
print(marks)
marks["parth"] = 97
print(marks)
marks["mote"] = 100
print(marks)
