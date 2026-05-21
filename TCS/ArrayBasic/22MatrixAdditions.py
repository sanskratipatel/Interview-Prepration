A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]
ans=[]
if len(A) !=len(B) : 
    print("nOOOO")
else :
    for i in range(0 ,len(A) ) : 
        row = [] 
        for j in range(len(A[0])) :  
            row.append(A[i][j] + B[i][j]) 
        ans.append(row)
print(ans)