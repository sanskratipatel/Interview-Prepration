def ll_cycle_starting_point(head) : 
    slow = head 
    fast = head 

    while fast is not None and fast.next is not None : 
        slow = slow.next 
        fast = fast.next  

        if slow == fast : 
            slow = head 
            while slow !=  head : 
                slow = slow.next 
                fast = fast.next 
            return slow 
    return False