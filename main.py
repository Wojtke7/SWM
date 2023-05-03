import math
import random
import time
import numpy as np

# Lists from example
example_A = np.array([2, 3, 9, 2, 5, 1, 3, 7, 10])
example_B = np.array([2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10])

# Choose random amount of elements in both lists
random_range = random.randint(10, 10000)

# Fill both lists
A = np.random.randint(0, 20, random_range)
B = np.random.randint(0, 20, random_range)

print(f"Amount of elements: {random_range}")
print(f"List A: {A}")
print(f"List B: {B}")


# Function that checks if number is prime, time complexity sqrt(n)
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Main function, time complexity O(n * sqrt(n))
def func(seq_A, seq_B):
    set_B = set(seq_B)

    counter_B = {num_b: np.count_nonzero(seq_B == num_b) for num_b in set_B}

    # print(counter_B)

    C = [num_a for num_a in seq_A if not is_prime(counter_B.get(num_a, 0))]

    return C


# Execution
print("Starting function execution...")
start_time = time.time()

c = func(B, A)

end_time = time.time()
print("Function execution finished. \n")

duration = end_time - start_time
print(c)
print(f"Total time: {duration} \n")

# Execution from example
d = func(example_A, example_B)
print(f"Example from task: {d}")
