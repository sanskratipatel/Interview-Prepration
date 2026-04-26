class Movie: 
    def __init__(self,movie_name :str , total_seat : int , price :int): 
        self.movie_name = movie_name 
        self.total_seat = total_seat 
        self.price = price  
        self.booked_seat = 0 
    
    def booking(self , num_of_tickets) : 
        if self.total_seat -self.booked_seat < num_of_tickets :
            print(f"Sorry Not enough seats Availble") 
        else : 
            self.booked_seat = self.booked_seat + num_of_tickets 
            self.total_seat = self.total_seat - num_of_tickets 

    def show_status (self) : 
        seat_avl = self.total_seat - self.booked_seat  
        print(f"Movie Name = {self.movie_name}") 
        print(f"Seats Available {self.total_seat}") 
        print(f"Total Booked Seats {self.booked_seat}")


movie = Movie("Raaz" , 100 ,200) 
movie.show_status() 
movie.booking(20)
movie.show_status()