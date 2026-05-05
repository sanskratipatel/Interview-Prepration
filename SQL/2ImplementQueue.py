class Queue: 
    def __init__(self):
        self.items = [] 

    
    def is_empty(self) : 
        return len(self.items) == 0 
    
    def size(self) : 
        return len(self.items) 
    
    def enqueue(self, item) :  
        return self.items.append(item) 
    
    def dequeue(self) : 
        if len(self.items) == 0 :
            print("Queue is empty") 
            return  
        x = self.items.pop(0) 
        return x  
    
    def front(self) :
        if len(self.items) ==0 :
            print("Queue is Empty")  
            return 
        return self.items[0] 
    
    def rear(self):
        if len(self.items) ==0 : 
            print("Queue is Empty") 
            return 
        return self.items[-1] 
    
q1 =Queue() 
q1.enqueue(10) 
q1.enqueue(100) 
q1.enqueue(54) 
print(q1.dequeue()) 
print(q1.rear() ) 
print(q1.front()) 
print(q1.is_empty()) 
print(q1.size())

        
