def convert_from_celsius_to_farenhreit(c):
    fahrenheit = c*(9/5)+32
    return fahrenheit
celsius = float(input('Enter the temperature in Celsius to have converted: '))
converted_temperature = convert_from_celsius_to_farenhreit(celsius)
print(f'The temperature already converted is: {converted_temperature}')