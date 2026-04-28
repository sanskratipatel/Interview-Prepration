def oddEvenLinkedlist(head) : 
    even_head = head.next 
    even = head.next 
    odd =head 

    while even is not None and even.next is not None : 
        odd.next = odd.next.next 
        odd = odd.next 
        even.next = even.next.next  
        even = even.next 

    odd.next = even_head
