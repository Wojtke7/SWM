import math
import random
import time
import numpy

# Choose random amount of elements in both arrays
random_range = random.randint(10, 10000)

# Fill both arrays
A = numpy.random.randint(0, 10, random_range)
B = numpy.random.randint(0, 10, random_range)

print(f"Amount of elements: {random_range}")
print(A)
print(B)


# Function that checks if number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Main function
def func(seq_A, seq_B):
    C = []

    for num_a in seq_A:
        counter = 0

        for num_b in seq_B:
            if num_a == num_b:
                counter += 1

        if not is_prime(counter):
            C.append(num_a)

    return C


# Execution
print("Starting function execution...")
start_time = time.time()
c = func(A, B)
end_time = time.time()
total = end_time - start_time
print("Function execution finished.")

print(c)
print(f"Total time: {total}")
