import time
import math

# Define a simple timer decorator to measure execution time
def timer(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    print(f"{func.__name__} - n: {n} took {end_time - start_time:.8f} seconds")
    return result

def linear(n):
    return [i for i in range(n)]

def quadratic(n):
    if n > 5000:  # Adjusting to avoid impractical execution times
        print(f"Skipped {func.__name__} for n: {n} due to impracticality.")
        return "Skipped due to impracticality"
    return [(i, j) for i in range(n) for j in range(n)]

def cubic(n):
    if n > 5000:  # Adjusting to avoid impractical execution times
        print(f"Skipped {func.__name__} for n: {n} due to impracticality.")
        return "Skipped due to impracticality"
    return [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

def exponential(n):
    if n > 500:  # Adjusting to avoid impractical execution times
        print(f"Skipped {func.__name__} for n: {n} due to impracticality.")
        return "Skipped due to impracticality"
    return 2 ** n

def logarithmic(n):
    return math.log(n)

def factorial(n):
    if n > 500:  # Adjusting to avoid impractical execution times
        print(f"Skipped {func.__name__} for n: {n} due to impracticality.")
        return "Skipped due to impracticality"
    return math.factorial(n)

# List of n values to test
n_values = [10, 100, 500, 1000, 5000, 10000, 100000]

# Function list
functions = [linear, quadratic, cubic, exponential, logarithmic, factorial]

# Execute and time each function individually for each n value
for function in functions:
    for n in n_values:
            timer(function, n)
