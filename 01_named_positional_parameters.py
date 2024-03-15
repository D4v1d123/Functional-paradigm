# NAMED PARAMETERS (**kwargs) => They are parameters that can admit an indefinite 
# number of arguments with a key (in a dictionary), thus improving their clarity, 
# adaptability and scalability. They should be used in functions that will evolve 
# over time (this is a good  practice). 

#.     Named parameter.
#             ↓
def addition(**kwargs):
    return sum(kwargs.values())


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
print(f"Result: {result}. \n")

# POSITIONAL PARAMETERS (*args) => Unlike the named parameters, the positional 
# parameters can admit a indefinite number of arguments without keys associated
# to each value (in a tuple).

#   Positional parameter.
#            ↓
def addition(*args):
    return sum(args)


result = addition(103, 334)
print(f"Result: {result}.")

result = addition(103, 334, 43, 102, 54)
print(f"Result: {result}.")