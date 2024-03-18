# POSITIONAL ARGUMENTS => Arguments are passed in the order of the parameters defined
# in the function signature.
def division(num1, num2):  # Signature function.
    print(f"num1 = {num1}. \nnum2 = {num2}. \nResult = {num1 / num2}.\n")


print("POSITIONAL ARGUMENTS:")
# division(num1, num2).
#           ↓    ↓
division  (100, 20)
division  (20, 100)


# KEYWORD ARGUMENTS => Function parameter name (keyword) is defined with the argument
# to be assigned, this allows the arguments to be assigned in an different order that
# the signature function. This allows you to avoid logic errors due to incorrect 
# arguments assignment.
def division(num1, num2):  # Signature function.
    print(f"num1 = {num1}. \nnum2 = {num2}. \nResult = {num1 / num2}.\n")


print("KEYWORD ARGUMENTS:")
#          Keyword or parameter name.
#                     ↓        
division(num1 = 100, num2 = 20)
division(num2 = 20, num1 = 100)


# POSITIONAL VARIABLE PARAMETER OR ITERABLE UNPACKING (*args) => Unlike the named 
# parameters, the positional parameters can admit a indefinite number of arguments
# without keys associated to each value (in a tuple).
# Positional variable parameter.
#            ↓
def addition(*args):
    return sum(args)


print("POSITIONAL VARIABLE PARAMETER:")
result = addition(103, 334)
print(f"Result: {result}.")

result = addition(103, 334, 43, 102, 54)
print(f"Result: {result}.\n")


# NAMED PARAMETERS OR DICTIONARY UNPACKING (**kwargs) => They are parameters that
# can admit an indefinite number of arguments with a key (in a dictionary), thus 
# improving their clarity, adaptability and scalability. They should be used in 
# functions that will evolve over time (this is a good practice). 
#      Named parameter.
#             ↓
def addition(**kwargs):
    return sum(kwargs.values())


print("NAMED PARAMETERS:")
result = addition(
    a = 103,
    b = 334
)
print(f"Result: {result}.")

result = addition(
    a = 103,
    b = 334,
    c = 43,
    d = 102,
    e = 54
)
print(f"Result: {result}.")