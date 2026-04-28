def remove_nth_node_from_last(head ,n) : 
    temp = head 
    length = 0 
    while (temp is not None) :  
          temp = temp.next 
          length = length +1  
    if length == n : 
         new_head = head.next 
         del head 
         return new_head 
    
    ps = length - n 
    temp = head 
    count = 1 
    while count < ps: 
         count = count +1 
         temp = temp.next 

    temp.next = temp.next.next 
    return head

          

