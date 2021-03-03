from cs506 import *
import numpy as np
import numpy.linalg
from random import randint

'''
the following functions are from cs506/det.py
def det(A):

    rows = len(A)
    cols = len(A[0])
    if rows!=cols:
        raise ValueError("must be a square matrix")
    if rows == 1 and cols == 1:
        return A[0][0]
    res = 0
    for c in range(cols):
        cur = ((-1)**(1+c+1))*A[0][c]*(det(Aij(A,i=0,j=c)))
        res = res + cur
    return res

def Aij(A,i,j):
    rows = len(A)
    cols = len(A[0])
    res = []
    for r in range(rows):
        if r ==i:
            continue
        temp_row = []
        for c in range(cols):
            if c == j:
                continue
            temp_row.append(A[r][c])
        res.append(temp_row)
    return res
'''


def test_det():
    # testcases form lab section
    assert det([[4,3],[6,3]])==-6
    assert det([[1,3,2],[1,1,4],[2,2,1]])==14
    assert det([[3,4,5,6],[2,3,1,5],[5,6,4,2],[4,5,2,4]])==-15
    n=randint(1,10) # generate the num_row and num_cols of a random matrix
    random_matrix = np.random.randint(10, size=(n, n))
    assert det(random_matrix)==round(np.linalg.det(random_matrix))

test_det()