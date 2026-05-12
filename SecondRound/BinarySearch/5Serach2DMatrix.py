def search_matrix(arr , target) : 
   startnow = 0 
   end_row = len(arr)-1 
   row = len(arr) 
   n = len(arr[0])
   while startnow <= end_row : 
      mid = startnow + (end_row- startnow)//2 

      if target >= arr[mid][0] and target <= arr[mid][n-1]:
         
