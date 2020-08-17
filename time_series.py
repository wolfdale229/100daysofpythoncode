from typing import TextIO
def skip_header(reader:TextIO)-> str:
    """Skip the header in reader and return the first real piece of data.
    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
    >>> skip_header(infile)
    'Data line\\n'
"""
    # Skip over the description 
    line = reader.readline()
    
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
    
    return line

def find_largest(line:str)->int:
    '''Return the largest value in line, which is a whitespace-delimited string of integers that
    each end with a '.'.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    '''
    largest = -1
    for value in line.split():
        value = int(value[:-1])
        if value > largest:
            largest = value
    return largest


