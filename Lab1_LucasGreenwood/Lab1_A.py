# Part A : Convert celsius to fahrenheit

# prompt and read the input from the user, cast the string given into a float
temp_celsius = float(input("Enter the temperature in Celsius: "))

# calculate the conversion from Celsius to Fahrenheit
# FORMULA:
# F = (9/5) * C + 32
temp_fahrenheit = (9/5) * temp_celsius + 32

# print the converted temperature with an f string rounding to 1 decimal place
print(f"That is {temp_fahrenheit:.1f} degrees Fahrenheit!")
