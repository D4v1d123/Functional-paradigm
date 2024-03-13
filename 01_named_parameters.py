# NAMED OR POSITIONAL PARAMETERS => They are parameters that can admit an indefinite
# number of arguments, thus improving their clarity, adaptability and scalability. 
# they should be used in functions that will evolve over time (this is a good 
# practice). 

# Positional parameter
#        ↓
def sum(**numbers):
    result = 0
    for key in numbers:
        result += numbers[key]
    
    return result


result = sum(
    a = 103,
    b = 334
)
print(f"Result: {result}.")

result = sum(
    a = 103,
    b = 334,
    c = 43,
    d = 102,
    e = 54,
)
print(f"Result: {result}.")

