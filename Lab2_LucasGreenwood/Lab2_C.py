# Part A : Convert celsius to fahrenheit

# conversion function declaration
# calculate the conversion from Fahrenheit to Celsius:
def fahrenheit_to_celsius(temp_fahrenheit):
    return (5/9) * (temp_fahrenheit - 32)


# calculate conversion from Kelvin to Celsius:
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15


# calculate conversion from Celsius to Kelvin:
def celsius_to_kelvin(temp_celsius):
    return temp_celsius + 273.15


# calculate the conversion from Fahrenheit to Kelvin:
def fahrenheit_to_kelvin(temp_fahrenheit):
    return (5/9) * (temp_fahrenheit - 32) + 273.15


# calculate the conversion from Celsius to Fahrenheit:
def celsius_to_fahrenheit(temp_celsius):
    return (9/5) * temp_celsius + 32


# calculate the conversion from Kelvin to Fahrenheit
def kelvin_to_fahrenheit(temp_kelvin):
    return (9/5) * (temp_kelvin - 273.15) + 32


# read user inputs
unit_from = input("Enter the unit you are converting from: ").lower()
unit_to = input("Enter the unit you are converting to: ").lower()
unit_from_cap = unit_from[0].upper() + unit_from[1:]
unit_to_cap = unit_to[0].upper() + unit_to[1:]
reading = float(input(f"Enter the temperature in {unit_from_cap}: "))


if unit_from == 'celsius' and unit_to == 'fahrenheit':
    result = celsius_to_fahrenheit(reading)
elif unit_from == 'celsius' and unit_to == 'kelvin':
    result = celsius_to_kelvin(reading)
elif unit_from == 'fahrenheit' and unit_to == 'celsius':
    result = fahrenheit_to_celsius(reading)
elif unit_from == 'fahrenheit' and unit_to == 'kelvin':
    result = fahrenheit_to_kelvin(reading)
elif unit_from == 'kelvin' and unit_to == 'celsius':
    result = kelvin_to_celsius(reading)
elif unit_from == 'kelvin' and unit_to == 'fahrenheit':
    result = kelvin_to_fahrenheit(reading)
else:
    result = reading

# print the converted temperature with an f string rounding to 1 decimal place
print(f"That is {result:.1f} degrees {unit_to_cap}.")
