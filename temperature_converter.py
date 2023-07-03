'''
The code below asks the temperature in your place and calculates it to Fahrenheit and Kelvin
'''

print('''
        Temperature Converter

        Type the temperature, whats the scale you want to converter from
        and the final scale
''')

def get_info():
    value_list = []

    while len(value_list) < 1:
        try:
            value = float(input("Value: "))
            initial_base = int(input('''Whats the initial base?
                                Type 1 for Celsius
                                    2 for Fahrenheit
                                    3 for Kelvin
                                    --> '''))
            value_list.append(value)
    
        except:
            print("Invalid Value. Try again: ")
    
    return value, initial_base


def temp_converter(value, initial_base):
    if initial_base == 1:
        print(f'''{value} Celsius is equal to:
                  {(value * 9 + 160) / 5:.2f} Fahrenheit
                  {value + 273.15:.2f} Kelvin''')       
         
    elif initial_base == 2:
        print(f'''{value} Fahrenheit is equal to:
                  {(value - 32) * 5 / 9:.2f} Celsius
                  {((value - 32) * 5/9) + 273.15:.2f} Kelvin''')
        
    elif initial_base ==  3:
        print(f'''{value} Kelvin is equal to:
                  {value - 273.15:.2f} Celsius
                  {(value - 273.15) * 9/5 + 32:.2f} Fahrenheit''')
    

value, initial_base= get_info()
temp_converter(value, initial_base)