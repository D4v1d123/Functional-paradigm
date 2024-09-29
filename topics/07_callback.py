# CALLBACK FUNCTIONS => It is an arrow (in JavaScript), anonymous or named functions
# that is passed as an argument to other function, and is executed after an action 
# or event occurs. These types of functions are mainly used in asynchronous 
# programming with the objective of handling events or tasks.

def add(num1, num2, callback):
    result = num1 + num2  # Action (add numbers).
    callback(result)  # Call to callback (show the result after the action occurs).
    
def show_result(result):  # Callback or named function.
    print(f"The result is {result}\n")


print("EXAMPLE OF A CALLBACK WITH A NAMED FUNCTION:")
# Callback (without invoking) passed as an argument.
#              ↓
add(2, 4, show_result)

print("EXAMPLE OF A CALLBACK WITH AN ANONYMOUS FUNCTION:")
#          Callback or anonymous function passed as an argument.  
#                                 ↓
add(2, 4, (lambda result : print(f"The result is {result}\n")))

