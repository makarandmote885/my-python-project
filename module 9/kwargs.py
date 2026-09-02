# **kwargs --- dictionary
# many key value pairs
def student(**details):
    print(details)
student(name="makarand",age=21)    

#accessing values
def student(**details):
    print(details["name"])
    print(details["age"])
student(name="Makarand" , age=31)    
