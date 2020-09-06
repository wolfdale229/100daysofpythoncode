"""Test the task data type"""
from collections import namedtuple

Task = namedtuple("Task", ["summary", 'owner', 'done', 'id'])
Task.__new__.__defaults__ = ( None, None, False, None)


def test_defaults()-> None:
    """passing no argument invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access()->None:
    """Test if the .attribute for Task works"""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
