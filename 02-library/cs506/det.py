def det(M):
    rows=len(M)
    cols=len(M[0])
    if rows!=cols:
        print("What you input is not a square matrix")
    else:
        if rows==1 and cols==1:
            return M[0][0]
        else:
            res=0
            for n in range(cols):
                res+=(-1)**(1+n+1)*M[0][n]*det(Aij(M, i=0, j=n))
    return res


def Aij(M,i,j):
    rows=len(M)
    cols=len(M[0])
    res=[]
    for x in range(rows):
        if x==i:
            continue
        else:
            temp_row=[]
            for y in range(cols):
                if y==j:
                    continue
                else:
                    temp_row.append(M[x][y])
            res.append(temp_row)
    return res

#det of A is -1
A=[
[2,5],[3,7]
]
#det of B is 9
B=[
    [1,2,3],
    [4,5,6],
    [0,1,-1]
]
print('A: ',det(A))
print('B: ',det(B))