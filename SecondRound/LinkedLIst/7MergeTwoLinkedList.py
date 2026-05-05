def Merge_two_linked_list(h1 , h2) :  
    if h1 is None or h2 is None : 
        if h1 is None :
            return h2 
        else :
            return h1
    if h1.head <= h2.head :  
        h1.next = Merge_two_linked_list(h1.next , h2) 
        return h1 
    else : 
        h2.next = Merge_two_linked_list(h1 , h2,next) 
        return h2
