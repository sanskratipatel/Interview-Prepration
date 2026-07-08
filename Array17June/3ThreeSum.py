

class Solution:
    def triplets(self, arr ):
        # code here  
        ans = [] 
        set_ans = set()
        main_ans = []
        for i in range(0 , len(arr)) : 
            for j in range(i+1 , len(arr)) : 
                ans= []
                for k in range(j+1 , len(arr)) : 
                    if arr[i] + arr[j] + arr[k] == 0 :  
                        ans = [arr[i] ,arr[j] ,arr[k]]
                        ans = sorted(ans) 
                        set_ans.add(tuple(ans) )
        for i in ((set_ans)) : 
            main_ans.append(list(i) )
        main_ans.sort()
        return main_ans
    
        
