def det(A):
    """
    A is a square matrix in form of a lists 
    """
    rows = len(A)
    cols = len(A[0])
    assert rows == cols
    if rows == 1 and cols == 1:
        return A[0][0]
    res = 0
    for c in range(cols):
        res = res + ((-1)**(1+c+1))*A[0][c]*det(Aij(A, i=0, j=c))
    return res

def Aij(A, i, j):
    rows=len(A)
    cols=len(A[0])
    res=[]
    for r in range(rows):
        if r==i:
            continue
        temp_row=[]
        for c in range(cols):
            if c==j:
                continue
            temp_row.append(A[r][c])
        res.append(temp_row)
    return res

A = [[1,2],[2,3]]
print(det(A))