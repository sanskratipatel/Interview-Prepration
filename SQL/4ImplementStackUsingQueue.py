from collections import deque
class Using_Stack_queue: 
    def __init__(self):
        self.queue = deque()

    def push(self,item) : 
        self.queue.append(item) 
        for i in range(len(self.queue) -1 ): 
            self.queue.append(self.queue.popleft()) 


    def pop(self):
        if len(self.queue) ==0 :
            print("Stack is empty") 
            return 
        return self.queue.popleft() 
    
    def peek(self) :
        if len(self.queue) ==0 :
            print("Stack is empty") 
            return 
        return self.queue[0] 
    
    def is_empty(self) :
        return len(self.queue) ==0 
    
    def size(self) :
        return len(self.queue)


 