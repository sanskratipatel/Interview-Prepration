
# def main_func(node) : 
#     dia = 0 
#     def diameter_binary_tree(node , dia) : 
#         if node is None : 
#             return 
#         lh = diameter_binary_tree(node.left) 
#         rh = diameter_binary_tree(node.right) 
#         dia = max(dia, lh+rh) 

#         return 1 + max(lh, rh)  
#     diameter_binary_tree(dia , node) 



def main_func(node) : 
    dia = 0 
    def diameter_binary_tree(node , dia) : 
        if node is None:
            return
        lh = diameter_binary_tree(node.left)
        rh= diameter_binary_tree(node.right)  
        dia = max(dia,lh+rh) 

        return 1+ max(lh,rh)
  