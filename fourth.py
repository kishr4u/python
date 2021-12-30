#functions
def describe_pet(animal_type="dog", pet_name="default harry"):
    print(f"\n I have a {animal_type}")
    print(f"]n name is {pet_name}")

#positional params
describe_pet("dog","jugy")
#keyword args
describe_pet(pet_name="toggy",animal_type="cat")
#default args
describe_pet()


def printss(*some_tupple):
    for s in some_tupple:
        print(f"some s {s}")
        
printss('julie','joggy','rudy')


#third.py is a module in python and we are importing specific func, use * to import all funcs in module
from third import test_func 
test_func()