def min_stack(val) :  
    items = [] 

    if len(items ) == 0 : 
        items.append([val ,val]) 
    else : 
        mini = min(items[-1][1] , val) 
        items.append([val,mini]) 

def get_min(items) : 
    if len(items) == 0 :
        return 0 
    else : 
       return items[-1][1] 
    
def top(items) : 
    if len(items) == 0 :
        return 0 
    else : 
       return items[-1][0] 

def remove(items) :
    if len(items) == 0 :
        return 0 
    else : 
       return items.pop()