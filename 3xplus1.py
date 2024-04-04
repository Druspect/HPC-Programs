import sys

initial_number = int(sys.argv[1])
n = initial_number
iterations = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    iterations += 1

print(iterations)
