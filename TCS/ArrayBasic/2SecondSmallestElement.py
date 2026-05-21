def second_smallest (arr) : 
    smallest = float("inf") 
    second_smallest = float("inf") 
    for i in range : 
        if arr[i] <= smallest : 
            second_smallest = smallest 
            smallest = arr[i] 
        elif arr[i] <= second_smallest and arr[i] >smallest : 
            second_smallest = arr[i] 
    return second_smallest