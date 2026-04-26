class Tree: 
    def __init__(self , val):
        self.val = val 
        self.left = None 
        self.right = None 

drinks = Tree("drinks") 
hot = Tree("hot") 
cold = Tree("cold") 
tea = Tree("tea") 
coffee = Tree("coffee") 
cola = Tree("cola") 
fanta = Tree("fanta") 

drinks.left = hot 
drinks.right = cold
cold.left = cola 
cold.right = fanta 
hot.left = tea 
hot.right = coffee 

print(drinks.left.val)