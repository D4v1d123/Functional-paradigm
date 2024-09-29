# MEMOIZATION => It’s a dynamic programming technique that stores previously 
# calculated results in a function to avoid calculating them agin, reducing the 
# execution time. Memoization should only be used into pure functions that are 
# called very frequently. 

from time import time

fib_result = {  # Memoization of fibonacci.
    0 : 0,
    1 : 1
}

def fibonacci_with_memoization(sequence_num):
    if not(sequence_num in fib_result):
        for series in range(2, sequence_num + 1):
            if not(series in fib_result):
                fib_result[series] = fib_result[series - 1] + fib_result[series - 2]
    
    return fib_result[sequence_num]

def fibonacci_without_memoization(sequence_num):
    a, b = 0, 1
    
    for _ in range(1, sequence_num):
        aux = b
        b += a
        a = aux
    
    return b

def speed_test(func, arg):
    start = time()
    for _ in range(0, 1000000):
        result = func(arg)
    end = time() 
    
    return result, (end - start)


func_1 = fibonacci_with_memoization
func_2 = fibonacci_without_memoization

result, time_exec = speed_test(func_1, 150)
print(f"WITH MEMOIZATION. \nResult: {result} in {time_exec} seconds.\n")

result, time_exec = speed_test(func_2, 150)
print(f"WITHOUT MEMOIZATION. \nResult: {result} in {time_exec} seconds.\n")
