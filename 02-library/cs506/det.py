def det(A):
    rows = len(A)
    cols = len(A[0])
    assert rows == cols, "A must be a square matrix"

    if rows == 1 and cols == 1:
        return A[0][0]
    
    res = 0
    for c in range(cols):
        # c starts from 0
        res += (-1)**(1+c+1)*A[0][c]*det(A_ij(A, i=0, j=c))

    return res


def A_ij(A, i, j):
    rows = len(A)
    cols = len(A[0])
    res = []
    for r in range(rows):
        if r == i:
            continue
        temp_row = []
        for c in range(cols):
            if c == j:
                continue
            temp_row.append(A[r][c])
        res.append(temp_row)
    return res

A = [[4,3],[6,3]] 
# det(A) = 4*3-3*6=-6
B = [[1,2,3],[1,2,3],[4,5,6]]

print(det(A))
print(det(B))