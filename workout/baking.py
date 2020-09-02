import temperature

def get_baking_temperature(temp:float)-> str:
    '''Shows what the temperature would be in celsius if the baking instruction is in fahrenheit

    >>> get_baking_temperature(500)
    'Preheat oven to 500 degrees F (260 degrees C )'
    '''

    cel = str(temperature.convert_to_celsius(temp))
    temp = str(temp)
    return 'Preheat oven to'+temp+' degrees F (' +cel+ ' degrees C)'

fahr = float(input('Enter the bking temperature in fahrenheit : '))
print(get_baking_temperature(fahr))



