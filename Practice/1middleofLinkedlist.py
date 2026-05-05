def Middle_element(head) : 
    temp = head 
    count = 0  

    while temp is not None : 
        temp = temp.next 
        count = count+1 
    temp = head
    for i in range(0 , count//2) : 
        temp = temp.next 
    return temp 


def Slow_FastLinkedList(head) : 
    slow = head  
    fast = head 
    while fast is not None and fast.next is not None :
        fast = fast.next.next 
        slow =  slow.next

    return slow 

