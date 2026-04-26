def generate_permutation_string(str1  , idx = 0 , ans = None ) :  
    if ans is None : 
        ans = []
    str1 = list(str1)
    def solver(str1 , idx):
        if len(str1) == idx : 
            ans.append("".join(str1)) 
            return  
        for i in range(idx , len(str1)): 
            str1[idx] , str1[i] = str1[i] ,str1[idx] 
            solver(str1, idx+1 ) 
            str1[idx] , str1[i] = str1[i] ,str1[idx]   
    solver(str1 , idx)
    return ans 


str1 = "abc" 
ans = "" 
print(generate_permutation_string(str1 ) )