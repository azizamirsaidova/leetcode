def sparse__matrix(mat1, mat2):

    answer = [[0]*len(mat1[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                answer[i][j] += mat1[i][k] * mat2[k][j]
    return answer

mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(sparse__matrix(mat1, mat2))