# PURE FUNCTION => These functions use only their parameters to generate a result, 
# not affecting the state of the program. Furthermore, they always produce the same
# result with the same arguments. 

def sum(num_1, num_2):
    return num_1 + num_2


print(f"PURE FUNCTION. \n2 + 4 = {sum(2, 4)}.")
print(f"2 + 4 = {sum(2, 4)}.")  # Same result. 
print(f"2 + 4 = {sum(2, 4)}. \n")


# These functions use their parameters and the environment variables to generate a 
# response. Furthermore, they produce different results with the same arguments, 
# making it more difficult to predict their behavior, due to this, it’s recommended
# not to use impure functions in the possible (this is a good practice).
num_1 = [2]

def sum(num_2):
    num_1[0] += num_2
    return num_1[0]


print(f"IMPURE FUNCTION. \n2 + 4 = {sum(4)}.")
print(f"2 + 4 = {sum(4)}.")  # Different results. 
print(f"2 + 4 = {sum(4)}.")