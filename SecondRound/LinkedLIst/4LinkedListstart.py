def starting_linkedlist(head) : 
    slow  = head 
    fast = head 
    while fast is not None and fast.next is not None : 
        fast = fast.next.next 
        slow = slow.next 
        if slow == fast : 
            slow = head 
            while slow != fast : 
                slow = slow.next 
                fast = fast.next 
        return slow.val 
    
    