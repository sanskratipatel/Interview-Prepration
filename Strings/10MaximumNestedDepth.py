# Maximum Depth of Nested Parentheses 

str1 = "((())+(8)))"  
max_depth = 0 
my_stack = [] 
current_depth = 0 

for i in range(0 , len(str)): 
    if str1[i] == '(': 
        my_stack.append(str1[i]) 
        current_depth = current_depth +1 
        max_depth = max(max_depth ,current_depth) 
    elif str1[i] == ')': 
        my_stack.pop() 
        current_depth = current_depth -1  

print(max_depth)