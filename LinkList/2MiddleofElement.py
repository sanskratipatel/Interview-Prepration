
class LL:
    def MIddleLinkedList(self):
        temp = self.head 
        n = 0 
        while(temp is not None) : 
            temp = temp.next 
            n= n+1 
        temp = self.head
        for i in range( 0 , n//2): 
            temp = temp.next 
        print(temp)

