from typing import Callable, Any
var  = "Hello world"
print (var)
print ("Hej Chris")
print ("Hej Krull")


# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse","Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return f"{benefit} is a benefit of funtion"

def name_the_benefits_of_functions():

    for benefit in list_benefits():
        print(build_sentence(benefit))

name_the_benefits_of_functions()