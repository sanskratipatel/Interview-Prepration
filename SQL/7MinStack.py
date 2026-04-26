class MinStack: 
    def __init__(self):
        self.items = [] 

    def push(self, item) : 
        if len(self.items) == 0 :
            self.append([self.item , self.item]) 
        else : 
            mini = min(self.items[-1][1] ,item) 
            self.items.append([item , mini])
    def get_min(self): 
        """Get minimium in o(1)""" 
        if len(self.items) == 0 : 
            return 0 
        return self.items[-1][1] 
    
    def top(self) : 
        if len(self.items) == 0 : 
            return 0 
        return self.items[-1][0] 
    

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()[0]

    