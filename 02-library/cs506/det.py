# Implementing a function to determine the determinant of a square matrix

def det(A):
    """ A is a square matrix (nxn) represented by a list of lists
        ex: If A 2x2: [[1,2], [3, 4]]
        ex: If A 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        Note that mathematically, rows/columns are labeled starting with 1, 
        but written in code, rows/columns are labeled starting with 0.
    """
    rows = len(A)
    cols = len(A[0])
    determinant = 0
    if rows == 1 and cols ==1:
        # base case reached- A is 1x1
        return A[0][0]
    for c in range(cols):
        # recursively determine determinant
        determinant = determinant + (-1)**(1+c+1)*A[0][c]*det(A_ij(A, i=0, j=c))
    return determinant

def A_ij(A, i, j):
    """ helper function to return a matrix that removes the
        ith row and jth column of A
    """
    rows = len(A)
    cols = len(A[0])
    res = []
    for r in range(rows):
        if r==i:
            continue
        temp = []
        for c in range(cols):
            if c==j:
                continue
            temp.append(A[r][c])
            res.append(temp)
    return res