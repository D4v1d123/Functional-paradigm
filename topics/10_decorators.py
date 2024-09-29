# DECORATORS => These are functions that receive another function as an argument, 
# to add extra behavior without modifying it’s source code, then the decorator 
# return another function (function received as a parameter plus the extra 
# behavior), this to saving time in the implementation common behavior to many 
# functions at the same time (this is a good practice).

import time

def exec_time(func):  # Decorator.
    def calc_time(*args, **kwargs):  # Internal function.
        start = time.time() #            <-╻
        result = func(*args, **kwargs) # <-│
        end = time.time() #              <-│ => Extra behavior added.
        return result, (end - start) #   <-╹

    return calc_time


@exec_time  # Decorator applied to a function (addition). 
def addition(num_1, num_2):
    return num_1 + num_2

@exec_time
def subtraction(num_1, num_2):
    return num_1 - num_2

@exec_time
def multiplication(num_1, num_2):
    return num_1 + num_2

def division(num_1, num_2):
    return num_1 + num_2


print("WITH DECORATOR.")
result, alg_time = addition(2, 4)
print(f"2 + 4 = {result}, it calculated in {alg_time} seconds.")

result, alg_time = subtraction(2, 4)
print(f"2 - 4 = {result}, it calculated in {alg_time} seconds.")

result, alg_time = multiplication(2, 4)
print(f"2 * 4 = {result}, it calculated in {alg_time} seconds. \n")

print("WITHOUT DECORATOR.")
result = division(2, 4)
print(f"2 / 4 = {result}.")