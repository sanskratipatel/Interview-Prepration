# first =None 
# temp = head 

# second = temp.next 
# temp.next = first 
# first = temp 
# temp = second

def linledlistcycle(head) : 
    slow = head 
    fast = head 

    while fast is not None and fast.next is not None : 
        fast = fast.next.next 
        slow = slow.next 
        if fast == slow : 
            print("Cycle is involved")  
            break
