def find_maximum(numbers):
    # Initialize the first number in list as maximum
    max_number = numbers[0]

    # Loop through each number in the list
    for num in numbers:
        # If this number is larger than the current maximum, update the maximum
        if num > max_number:
            max_number = num

    # Return the maximum number
    return max_number


# Testing the function
numbers = [5, 10, 15, 20, 25]
print("The maximum number in the list is:", find_maximum(numbers))