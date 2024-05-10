# CLOSURE => It's a function within another function, this allows the internal
# function to access variables from the outer function.
def outer_function(number_1):
    def inner_function(number_2):  # This is a closure
        return number_1 + number_2
    
    return inner_function

function_closure = outer_function(5)

result = function_closure(2)  # 5 + 2 = 7
print(f"The result is: {result}")  

result = function_closure(6)  # 5 + 6 = 11
print(f"The result is: {result}\n")  