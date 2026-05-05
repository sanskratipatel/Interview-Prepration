def reverse_linked_list(head): 
    if head is None :  
        print("ll is None") 
        return 
    else : 
        temp = head 
        prev= None 
        while temp is not None: 
            curr = temp.next 
            temp.next= prev 
            prev = temp 
            temp = curr 
        return temp
