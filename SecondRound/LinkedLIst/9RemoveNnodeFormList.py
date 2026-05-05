def remove_N_node_list(head , n) : 
    slow = head 
    fast = head 
    for i in range(0 , len(n)) : 
        fast = fast.next 
    
    if fast is None :
        return head.next 
    
    while fast.next is not None : 
        slow = slow.next 
        fast = fast.next 
    
    slow.next =slow.next.next 