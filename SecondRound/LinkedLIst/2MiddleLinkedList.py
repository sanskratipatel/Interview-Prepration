def middle_linked_list(head ): 
    if head is None : 
        print("LL is empty") 
        return 
    else : 
        slow = head
        fast = head 
        while fast is not None and fast.next is not None : 
            fast = fast.next.next 
            slow = slow.next  
        return slow.val