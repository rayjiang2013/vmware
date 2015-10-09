'''
Created on Oct 8, 2015

@author: ljiang
'''
import pytest
from max_sum import *

@pytest.mark.parametrize("list, expected", [([-1,5,-4,-2,6,5,-4,3,-8,9], (4, 5)), ([-3,-2,-1], (2, 2)), ([0,0,0], (0, 0))])
def test_largeSubarray(list, expected):
    assert largeSubarray(list) == expected
    
@pytest.mark.parametrize("list, expected", [([-1,5,-4,-2,6,5,-4,3,-8,9], (4, 5)), ([-3,-2,-1], (2, 2)), ([0,0,0], (0, 2)), ([-1,0,0,1], (3, 3)), ([-3,-2,-1,5], (3, 3)), ([-3,-2,-1,-5], (2,2)), ([0,1,2], (0, 2))])
def test_largeSubarray_2(list, expected):
    assert largeSubarray_2(list) == expected