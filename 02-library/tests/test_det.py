import pytest
from cs506 import det

def test_det():
    try:
         det.det([1,2,3], [4,5,6])
    except IndexError as e:
        assert str(e) == "Matrices must be square"

        assert det.det([1,2,3], [4,5,6], [7,8,9]) == 0
        assert det.det([1,2], [4,5]) == -3
