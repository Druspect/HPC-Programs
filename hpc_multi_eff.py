import multiprocessing
import numpy as np
import timeit
import cProfile
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fibonacci(n):
    """Calculate the nth Fibonacci number. Simple recursive approach for demonstration."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def parallel_fibonacci(n):
    """Calculate Fibonacci in parallel."""
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(fibonacci, [n]*multiprocessing.cpu_count())
    return result

def matrix_multiplication(size=100):
    """Perform matrix multiplication on two randomly generated matrices of specified size."""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    start_time = time.time()
    np.dot(A, B)
    end_time = time.time()
    logging.info(f"Matrix multiplication for size {size}x{size} completed in {end_time - start_time} seconds.")

def validate_input(n):
    """Validate input to ensure it is a positive integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return n

def main():
    n = 30  # Example value for Fibonacci calculation, adjust as necessary for testing
    matrix_size = 100  # Example size for matrix multiplication

    try:
        validated_n = validate_input(n)
        logging.info("Starting parallel Fibonacci calculation...")
        start_time = timeit.default_timer()
        fib_results = parallel_fibonacci(validated_n)
        elapsed = timeit.default_timer() - start_time
        logging.info(f"Parallel Fibonacci calculation completed in {elapsed} seconds. Results: {fib_results}")

        logging.info("Starting matrix multiplication test...")
        matrix_multiplication(matrix_size)

    except ValueError as e:
        logging.error(f"Validation Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
