# This program converts temperature from Fahrenheit to Celsius

# Taking temperature in Fahrenheit from user
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Converting temperature to Celsius
temp_celsius = (temp_fahrenheit - 32) * 5/9

# Printing the converted temperature
print("The equivalent temperature in Celsius is", temp_celsius)
