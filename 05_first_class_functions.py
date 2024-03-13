# FIRST CLASS FUNCTION => It's can be passed as a parameter to another function
# (higher-order function). This type of function can be returned within inside 
# function. This functions can be manipulated as variables. 
def addition(number_1, number_2):  # First class function.
    return number_1 + number_2

addition_function = addition  # Function object or function reference.
result = addition_function(2, 2)
print(f"The addition result is: {result}\n")
# ----------------------------------------------------------------------------
def greeting(name): print(f"Hi {name}\n")  # First class function.

def apply_function(function, value):  # Higher order function.
    return function(value)

apply_function(greeting, "Salamanca")


# map() => It allows you to apply a function to each item of an iterable data
# structure.  
students = ["Brayan", "Sonia", "Carlos", "Jessica"]

students_upper = list(map(str.upper, students))
print(f"Students in upper {students_upper}.\n")


# ANONYMOUS FUNCTION (lambda) => It's a short function without a name, these are 
# used for simples and single-use functionalities.
fruits = ["banana", "strawberry", "apple"]
suffix = "-fruit"

#                     Parameters    Return         
#                          ↓           ↓
fruits = list(map(lambda fruit : fruit + suffix, fruits))
print(f"The fruits are {fruits}.\n")


# filter() => It allow you, based on a conditional function, to filter data 
# from an iterable data structure.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pair_numbers = list(filter(lambda number : number % 2 == 0, numbers))
print(f"Pairs numbers are {pair_numbers}.\n")


# sorted() => It allow you to sort the items of an iterable data structure, this through 
# a function that returns a key or index of data to be sorted.
people = [
    ("Alejandra", 23, 3204217392),
    ("Santiago", 36, 3134389710),
    ("Alvaro", 45, 3184024639),
]

#                                                                           Optional parameter         
#                                                                                   ↓
persons_sorted_by_age = list(sorted(people, key = lambda person : person[1], reverse = True))
print(f"The people are {persons_sorted_by_age}.\n")


# reduce() => It allows you to reduce the values of an iterable to a value, this through a
# function that operates each item. 
from functools import reduce 

savings = [10000, 87000, 36000, 217000]

total_saving = int(reduce(lambda number_1, number_2 : number_1 + number_2, savings))
print(f"My savings are ${total_saving} COP.\n")