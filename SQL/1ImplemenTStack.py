class Stack:  
    def __init__(self ): 
        self.items = [] 

    def is_empty(self) : 
        return len(self.items) == 0 
    
    def push(self , item) : 
        self.items.append(item) 
    
    def pop(self) : 
        if len(self.items) == 0 : 
            print("Stack is empty") 
            return
        return self.items.pop()  
    
    def top(self) :
        if len(self.items) ==0 :
            print("Stack is Empty") 
            return
        return self.items[-1] 
    
    def size(self) :
        return len(self.items)  
    
s1 = Stack() 
s1.push(10) 
s1.push(20)
print(s1.is_empty() ) 
print(s1.top())
