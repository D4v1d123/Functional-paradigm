# MUTABLE DATA => They can modify their value after being created: List, 
# dictionaries, set and objects. These variables can be passed by reference to a 
# function.

# IMMUTABLE DATA => They can NOT modify their value after being created: Integer,
# float, string, tuple and bool. These variables can be passed by value to a 
# function.
def variable_in_upper(message, friends_list):
    message = message.upper()
    friends_list[0] = friends_list[0].upper()

message = "hello world"
friends_list = ["Mariana", "Alberto", "Camila"]

variable_in_upper(message, friends_list)
print(f"Immutable variable: {message} \nMutable variable: {friends_list}\n")