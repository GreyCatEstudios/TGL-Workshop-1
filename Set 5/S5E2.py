import time
import random


# Create the decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start} seconds")
        return result
    return wrapper


# Use the decorator on a function
@timer
def sort_random_numbers(n):
    numbers = [random.randint(0, 100) for _ in range(n)]
    numbers.sort()
    print(numbers)


# Call the function
sort_random_numbers(100)
