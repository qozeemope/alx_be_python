FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit) :
    temp_celcius = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_celcius

def convert_to_fahrenheit(celsius) :
    temp_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return temp_fahrenheit


convert_temp_input = input("Enter the temperature to convert: ")
if not convert_temp_input.isnumeric() :
    print("Invalid temperature. Please enter a numeric value.")
    exit()
convert_temp = int(convert_temp_input)

temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ") 

if temp_unit == "C":
    conversion = convert_to_fahrenheit(convert_temp)
    print(f"{convert_temp}°C is {conversion}°F")
elif temp_unit == "F":
    conversion = convert_to_celsius(convert_temp)
    print(f"{convert_temp}°F is {conversion}°C")