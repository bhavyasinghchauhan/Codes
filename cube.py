#take input
N = int(input())
if N<100 and N>1:
    mat=[]
    for i in range(N):
        m =input()
        g = m.split()
        mat.append(g)
    #Rotate wall

    def rotatewall(mat): 
        for x in range(0, int(N / 2)): 
            for y in range(x, N-x-1): 
                temp = mat[x][y] 
                mat[x][y] = mat[y][N-1-x] 
                mat[y][N-1-x] = mat[N-1-x][N-1-y] 
                mat[N-1-x][N-1-y] = mat[N-1-y][x] 
                mat[N-1-y][x] = temp 

    #find Maximum C sized walls that can be made
    rotatewall(mat) 
    for i in mat:
        i.sort(reverse=True)
    rotatewall(mat) 
    for i in mat:
        i.sort(reverse=True)
    rotatewall(mat) 
    for i in mat:
        i.sort(reverse=True)

    g=mat[0].count("C")
    print(g)