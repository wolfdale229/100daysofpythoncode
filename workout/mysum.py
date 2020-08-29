import unittest
from typing import Tuple
def mysum(numbers:list, starting:[int]=0)-> float:
    """Returns the sum of a list of number of different types
    """
    total = 0
    for item in numbers:
        total += item
    if starting:
        total += starting
    return total

class TestMySum(unittest.TestCase):
    """Test for function mysum"""
    
    def test_my_sum_empty(self):
        required = sum([])
        expected = mysum([])
        self.assertEqual(expected, required, 'Test for empty arguments')
        
    def test_my_sum_pos_values(self):
        """Test for all positive values"""
        required = sum([1, 2, 3,4])
        expected = mysum([1, 2, 3, 4])
        self.assertEqual(expected, required, 'Test for sum of list of numbers')

    def test_my_sum_zero(self):
        """test when the value is zero"""
        required = sum([0])
        expected = mysum([0])
        self.assertEqual(expected, required, 'Testing for zero')

    def test_my_sum_neg_values(self):
        """Test for all negative numbers"""
        required = sum([-1, -2, -6])
        expected = mysum([-1, -2, -6])
        self.assertEqual(expected, required, 'Testing for negative values')

    def test_my_sum_mixed_values(self):
        '''Test for both positive and negative values '''
        required = sum([-1, 2, -3, 6])
        expected = mysum([-1, 2, -3, 6])
        self.assertEqual(expected, required, 'Testing for mixed values')

    def test_my_sum_with_start(self):
        """Test when there is start parameter"""
        required = sum([1, 2, 3], 4)
        expected = mysum([1, 2, 3], 4)
        self.assertEqual(expected, required, 'Test with additional value')


if __name__ == '__main__':
    value = [1, 2, 3, 4]
    print(f'Answer : {mysum(value)}')
    unittest.main()
