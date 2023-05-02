import math
import random
import time
import numpy

# Choose random amount of elements in both arrays
random_range = random.randint(10, 10000)

# Fill both arrays
A = numpy.random.randint(0, 20, random_range)
B = numpy.random.randint(0, 20, random_range)

print(f"Amount of elements: {random_range}")
print(A)
print(B)


# Function that checks if number is prime
# Time complexity sqrt(n)
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Main function time complexity O(n * sqrt(n))
def func(seq_A, seq_B):
    set_A = set(seq_A)
    set_B = set(seq_B)

    counter_B = {num_b: numpy.count_nonzero(seq_B == num_b) for num_b in set_B}

    # print(counter_B)

    C = [num_a for num_a in set_A if not is_prime(counter_B.get(num_a, 0))]

    return C


# Execution
print("Starting function execution...")
start_time = time.time()

c = func(A, B)

end_time = time.time()
print("Function execution finished.")

duration = end_time - start_time
print(c)
print(f"Total time: {duration}")
