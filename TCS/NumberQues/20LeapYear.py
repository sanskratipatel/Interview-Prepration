def leap_year(year) : 
    if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0) :
        return f"Leap Year" 
    return f"Not leap Year"