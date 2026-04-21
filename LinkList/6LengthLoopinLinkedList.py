class LinkedList:
    def lengthLinkedList(self) : 
        temp = self.head  
        travel = 0 
        my_dict = {}
        while(temp is not None) :  
            if temp in my_dict : 
                ans = travel - my_dict[temp] 
                print(ans)
                break 
            else :  
                my_dict[temp] = travel 
                travel = travel +1  
                temp = temp.next

    def optimized(self) :
        slow = self.head 
        fast = self.head 
        count = 0 
        while(fast is not None and fast.next is not None):
            slow = slow.next 
            fast =fast.next.next 
            if slow == fast :
                slow = slow.next 
                count = 1 
                while slow != fast :
                    slow = slow.next 
                    count = count +1 
                print(count) 

      