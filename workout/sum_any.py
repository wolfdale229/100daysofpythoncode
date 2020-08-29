from doctest import testmod
def sum_any(values:list)-> int:
    """From a list containing values of diffenrent types, return the 
    sum of numerical values

    >>> value = [1, '2', '3', 'e']
    >>> sum_any(value)
    6
    >>> sum_any([10, '-9', 'o'])
    10
    >>> sum_any(['-1', '-9', 'omo'])
    0

    Note : it won't work for nagative numbers
    """
    total = 0

    for item in values:
        if isinstance(item, int) or str(item).isdigit(): #Check if each item is either of type int or a string of a number
            total += int(item)
    return total
print('The function call is in the doctest, read the code')
testmod()
