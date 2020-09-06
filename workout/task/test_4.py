""" Test the Task data type"""

from collections import namedtuple


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_adict()-> dict:
    """ Test if ._asdict() return a dictionary"""
    t_task = Task('do something', 'okken', True, 21)
    t_new = t_task._asdict() # t_new is a dictionary 
    expected = {'summary':'do something', 
                'owner' :'okken',
                'done': True, 'id' : 21}
    assert t_new == expected

def test_replace()-> None:
    """Test the replace() function changes passed fields"""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    expected = Task('finish book', 'brian', True, 10)
    assert t_after == expected

