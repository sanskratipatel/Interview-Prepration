def seggregate_odd_even(head) :
    odd = head 
    even=  head.next   
    even_node = even 

    while even is not None and even.next is not None: 
        odd.next = odd.next.next  
        odd = odd.next 
        even.next = even.next.next 
        even = even.next 
    
    odd.next = even_node

    



