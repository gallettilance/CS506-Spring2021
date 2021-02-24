import pytest
import random

from cs506 import det

def test_det():
    # sanity checks
    try:
        det.det([[1, 2], [2, 3], [3, 4]])
    except ValueError as e:
        assert str(e) == "A must be a square matrix"
    
    assert det.Aij([[1, 2, 3], [4, 5, 6], [7, 8, 9]], i=1, j=1) == [[1, 3], [7, 9]]
    assert det.det([[4, 3], [6, 3]]) == -6

    # all elements of a row is 0, determinant is 0
    assert det.det([[0, 0], [6, 3]]) == 0

    # determinant of identity matrix is 1
    assert det.det([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1

    # det(AT) == det(A)
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    AT = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert det.det(A) == det.det(AT)