def reverselinkedlist(head) : 
    first = None
   
    temp = head 
    while temp is not None : 
        second = temp.next
        temp.next = first 
        first = temp 
        temp = second
        
        