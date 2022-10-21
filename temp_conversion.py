
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    current_degree = 100
    celsius_100 = (current_degree - 32) * (5 / 9)
    print(celsius_100)
    print('float')
    # I believe this is going to be float because 5 / 9 doesn't return a whole number


def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    current_degree = 0
    celsius_0 = (current_degree - 32) * (5 / 9)
    print(celsius_0)


def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    print((34.2 - 32) * 5 / 9)

'''
Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    print((5 * (9 / 5)) + 32)


def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    print('30.2 degrees celsius')

# convert_100_to_celsius()
# convert_0_to_celsius()
# convert_34_2_to_celsius()
# convert_5_to_fahrenheit()
# hotter_temp()

def convert_to_celsius(num):
    print((num - 32) * 5 / 9)

def convert_to_fahrenheit(num):
    print((num * (9 / 5)) + 32)

def temperature_convert(num, degrees):
    if degrees == 'fahrenheit':
        convert_to_celsius(num)
    elif degrees == 'celsius':
        convert_to_fahrenheit(num)

temperature_convert(38, 'celsius')