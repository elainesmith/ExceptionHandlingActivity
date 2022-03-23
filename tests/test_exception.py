from random import random
import pytest

from activity.main import *

def test_exception_raise_index_error():
    #ARRANGE
    random_list = [1, 2, 3]

    #ASSERT
    with pytest.raises(IndexError):
        out_of_range_index(random_list)