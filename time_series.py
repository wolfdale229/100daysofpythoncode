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
