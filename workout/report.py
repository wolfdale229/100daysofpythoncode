def get_description()-> str:
    """ Picks a value of weather descriptions from the 
    list randomly
    """
    from random import choice

    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

