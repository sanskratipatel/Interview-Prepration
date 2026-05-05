class Queue_using_Stack: 
    def __init__(self):
        self.s1 =[] 
        self.s2 =[] 

    def enqueue(self , item) : 
        while self.s1  :
            self.s2.append(self.s1.pop()) 
        self.s1.append(item) 
        while self.s2 : 
            self.s1.append(self.s2.pop()) 
        
    def deqeue(self) : 
        if len(self.s1) == 0 : 
            print("Empty") 
            return 
        return self.s1.pop() 
    
