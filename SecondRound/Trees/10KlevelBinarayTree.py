def Klevel(node , k) :  
    if node is None : 
        return
    if k == 1 : 
        print(node.val , end = " ")
        return 
    Klevel(node.left , k-1) 
    Klevel(node.right , k-1) 

