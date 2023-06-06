# This program checks if a given number is prime or not

# Taking input from user
num = int(input("Enter a number: "))

# Assume the number is prime until proven otherwise
is_prime = True

# Check the divisibility of num starting from 2 to num - 1
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# Checking the boolean value of is_prime to determine output
if num < 2:  # the smallest prime number is 2
    print(num, "is not a prime number.")
elif is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
