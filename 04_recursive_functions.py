# RECURSIVE FUNCTIONS => It's a functions that is to calls itself, this with 
# objective of simulating a loop in a functional paradigm.

# BASE CASE => Condition to check if the recursive function has found the 
# answer.

# RECURSIVE CASE => Is the condition that allows the recursive function to 
# be called itself.
def loop(i):
    if i > 10:  # Base case or variable limit.
        return i

    # Recursive case. 
    print(f"Iteration {i}.")
    i += 1  # Increaser.   
    return loop(i)  # Recursive call.          


loop(0)
print("")


# Additionally, recursive functions allow you to solve problems that can be 
# break out into smaller problems until you find the answer.
def recursive_factorial(number):
    # Base case.
    if number == 0:
        return 1
    
    # Recursive case.
    return number * recursive_factorial(number - 1)  # Recursive call.   


print(f"Factorial of 8: {recursive_factorial(8)}.")
