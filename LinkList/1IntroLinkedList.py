class Node: 
    def __init__(self,val): 
        self.value = val 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None 
    def append(self,val) : 
        new_node = Node(val) 
        if self.head ==None : 
            self.head = new_node 
        else :  
            curr  = self.head
            while(curr.next != None) : 
                curr = curr.next

            curr.next = new_node 
    def Traversal(self) : 
        if self.head is None:
            print("It is Empty") 
        else : 
            curr = self.head 
            while(curr is not None) : 
                print(curr.value) 
                curr = curr.next   
    def insert_on_index(self, pos ,val) :  
        new_node = Node(val)
        if pos == 0  : 
            new_node.next = self.head 
            self.head = new_node
        else : 
            curr = self.head 
            prev = None 
            count = 0

            while(curr is not None and count < pos) : 
                prev = curr 
                curr = curr.next 
                count =count+1 

            prev.next =new_node 
            new_node.next = curr 
    def delete(self,pos) : 
        temp = self.head 
        if temp.val is not None : 
            self.head = temp.next 
            del temp 
        else :
            found = False 
            prev = None 
            while(temp is not None) :
                if temp.val == pos :
                    found = True  
                    break 
                prev = temp 
                temp = temp.next 
            
            if found : 
                prev.next = temp.next  
                del temp 
            else:
                print("Node Not found")



        
a = LinkedList()
a.append(10) 
a.append(12) 
a.append(13) 
a.Traversal()
a.insert_on_index(3,100)
a.Traversal()
a.insert_on_index(0,123)  

        