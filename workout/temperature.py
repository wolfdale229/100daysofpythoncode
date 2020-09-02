def convert_to_celsius(fahrenheit:float)->float:
    """Convert a given temperature value from unit farenheit to
    unit celsius
    
    >>> convert_to_celsius(75)
    23.88888888889
    >>> convert_to_celsius(-32)
    -35.5555555556
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def above_freezing(temp:float)->bool:
    """returns True if the temperature is above the freezing temperature

    >>> above_freezing(-09)
    False
    >>> above_freezing(100)
    True
    """
    return temp > 0

if '__name__' == '__main__':
    temp = float(input('Enter your temperature here : '))
    celsius = convert_to_celsius(temp)
    if above_freezing(celsius):
        print(f'{celsius} is above the freezing point')
    else:
        print('It is below the freezing point')

