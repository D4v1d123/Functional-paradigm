# GENERATING EXPRESSION => They are special function that, when call, process or 
# generate only one result at a time. Due to this, they reduce memory consumption
# and processing. They are used for sequential big data processing, filtering and 
# transforming data, finally, lazy generation (on demand) of results.

# These functions pause and save their state (they maintain the values of their local 
# variables),so they can process the next result when called. 

#                          Generating expression.
#                                    ↓
even_numbers = (num for num in range(1000) if (num % 2) == 0)
#     ↑        ↑                                            ↑
#     │        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# Generator  The generating expression is always in parenthesis.
#  object.

print("RESULTS OF THE GENERATING EXPRESSION:")
print(next(even_numbers))  #             <-╻
print(next(even_numbers))  #             <-│ => Generates or processes the following
print(next(even_numbers), end="\n\n")  # <-╹    result. 


def fibonacci():  # Generating function.
    a, b = 0, 1
    while True:
        yield a  # Make it only process and return one value at a time. 
        a, b = b, a + b

generator_fibonacci = fibonacci()
#        ↑       
# Generator object.

print("RESULTS OF THE GENERATING FUNCTION:")
print(next(generator_fibonacci))  #             <-╻
print(next(generator_fibonacci))  #             <-│ => Generates or processes the
print(next(generator_fibonacci), end="\n\n")  # <-╹    following result. 


def get_letters(text:list):  # Generating function with "yield from".
    for word in text:
        yield from word  # Loop through the iterable or word.
        
text = ["Yield", "from", "is", "a", "powerful", "and", "convenient", "way", "to", 
        "delegate", "iteration", "over", "an", "iterable", "within", "a", "generator,", 
        "simplifying", "code", "and", "improving", "readability."]

letters_generator = get_letters(text)
#        ↑       
# Generator object.

print("RESULTS OF THE GENERATING FUNCTION WITH \"YIELD FROM\":")
print(next(letters_generator))  # <-╻
print(next(letters_generator))  # <-│ => Generates or processes the following result. 
print(next(letters_generator))  # <-╹