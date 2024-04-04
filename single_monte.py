import random
import time

# Function to estimate Pi by simulating points within a square that encloses a quarter circle
def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1.0:
            inside_circle += 1
    return (4 * inside_circle) / num_samples

def main():
    num_samples = 10000000  # Total number of samples for the estimation
    print(f"Estimating Pi using {num_samples} samples")

    # Start timing the execution
    start_time = time.time()

    # Estimate Pi
    pi_estimate = estimate_pi(num_samples)
    print(f"Estimated Pi: {pi_estimate}")

    # End timing the execution
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
