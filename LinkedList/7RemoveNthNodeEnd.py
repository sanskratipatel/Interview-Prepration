def remove_nth_n_node_from_end(head , k ) :  
    
    temp = head 
    count = 0 
    while temp is not None : 
        temp = temp.next 
        count = count +1 
    temp = head
    if count == k : 
        new_head = head.next 
        del head 
        return new_head
    val = count - k 
    num = 0
    if val > 0 :
        while count < val :  
            temp = temp.next 
            count = count +1 
        temp.next = temp.next.next 
        return head     




