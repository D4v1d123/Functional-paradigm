# GLOBAL VARIABLE => It is declared outside of a function and can be accessed from 
# anywhere in the code, even in other modules or files.

# LOCAL VARIABLE => It is declared inside a function. It can only be accessed in of the 
# function, when the execution of all content of the function ends, the local variables 
# are removed.

# NONLOCAL VARIABLE => It is declared inside a main function that has another function 
# inside it (nested function). Non-local variables can be accessed within the inner 
# function (closure) of the main function.

name = "Danna"  # Global variable.

def greeting():
    lastname = "Garcia"  # Local variable.
    print(f"Hello {name} {lastname}")
    
def get_id(age):  # Main function.
    def define_id(age):  # Nested function.
        if age >= 18:
            print(f"Your citizenship card is {cc}")
        elif age >= 8:
            print(f"Your identity card is {ic}")
        else:
            print(f"Your civil registration is {cr}")
            
    cc = 89418921  #   <-╻
    ic = 1002348123  # <-│ => Non-local variable.
    cr = 1004312870  # <-╹  
    
    define_id(age)


greeting()
get_id(18)