def odd_even_linked_list(head) : 
    if head is None : 
        return head 

    if head.next is None : 
        return head 
    val = [] 
    temp = head
    while temp.next is not None : 
        val.append(temp.val) 
        temp = temp.next.next
    
    temp = head.next  
    while temp.next is not None : 
        val.append(temp.val) 
        temp = temp.next.next
    idx = 0 
    temp = head
    while temp is not None :  
        temp.val = val[idx] 
        temp = temp.next 
    
    return head

