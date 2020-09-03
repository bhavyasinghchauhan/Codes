A = [[10,10,0,0]] 

B = [[-1,3,-3,1], 
    [3,-6,3,0], 
    [-3,3,0,0],
    [1,0,0,0]] 
  
      
result = [[0, 0, 0, 0]]
def matrix_multiply(A,B):
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
    for r in result: 
        print(r) 
matrix_multiply(A,B)
