def length_of_linked_list(head) : 
    slow = head 
    fast = head 

    while fast is not None and fast.next is not None : 
        fast =fast.next.next 
        slow =slow.next 
        if slow ==fast : 
            count =1 
            slow = slow.next  
            while slow != fast : 
                slow = slow.next 
                count = count +1 

        return count 

