#Arguments with default values
#Standard value define in the function definition
#You can see when you put the pointer in the function and see "arg=..."

# def func_print(a=1,b=2,c=3):
#     print(a,b,c)
#
# func_print()

#Unlimited Position Arguments
#
# def print_unlimited(*args):
#     for n in args:
#         print(n)
# numbers = (item for item in range(1,101))
# print_unlimited(numbers)

# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(1,2,3,4,5))

#Preset default values with key words like dictionaries
#.get make return none if the attribute is empty
#Allow to create infinite attributes and their values

# class Car:
#     def __init__(self,**kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# new_car = Car(make="Volkswagen", model="Nivus")
# print(new_car.make,new_car.model)

def test(*args):
    print(args)

    type(*args)

test(1, 2, 3, 5)
