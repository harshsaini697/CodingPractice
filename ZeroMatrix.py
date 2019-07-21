def zeromatrix(M,N,mat):
    for i in range(M):
        if int(0) in mat[i]:
            mat[i]=[0]*N


    print(mat)

mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 0, 12 ],
        [13, 14, 15, 16 ] ]
zeromatrix(4,4,mat)