# This program prints the first 10 Fibonacci numbers

# Initial two numbers
num1, num2 = 0, 1

# Print first two numbers
print(num1)
print(num2)

# For the next 8 numbers
for _ in range(8):
    # Calculate the next Fibonacci number
    num_next = num1 + num2

    # Print the next number
    print(num_next)

    # Shift the last two numbers down the sequence
    num1, num2 = num2, num_next
