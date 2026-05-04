def reverse_linked_dllist(head): 
    temp = head 
    prev = None 
    while temp is not None : 
        curr = temp.next  
        temp.next = prev  
        temp.prev = curr  
        prev =temp 
        temp = curr 

    return prev  



