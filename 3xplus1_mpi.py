from mpi4py import MPI
import random
import sys

def collatz_iterations(initial_number):
    n = initial_number
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    for _ in range(100000000000 // size):  # Divide the total number of iterations by the number of MPI tasks
        initial_number = random.randint(1, 100000000000)
        iterations = collatz_iterations(initial_number)
        print(f"{initial_number},{iterations}")
