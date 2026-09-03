squ = lambda x : x*x 
print(squ(10)) 

my_dict = {"Apple" : 4 , "grapes" : 45 , "kiwi" : 1 , "oranges" : 10} 

# Sorted on the basis key aaple , kiwi 
res = sorted(my_dict.keys() ,key= lambda x : x[1] , reverse = True) 
print(res) 

# sorted on the basis value 
res1  = sorted(my_dict.values() , reverse = True) 
print(res1) 


numbers = [4,3,2,41] 

func = list(map(lambda x:x*2 ,numbers)) 
print(func)  

l2 = [5,4,2,6,5] 

func = list(map(lambda x : x +10 , l2) ) 
print(func)  

func1 = list(filter(lambda x: x%2 ==0 , l2)) 
print(func1) 


from functools import reduce 

func3 = reduce(lambda x,y : x + y , l2) 
print(func3)