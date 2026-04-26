from SingleResponsiblityPrinciple import User, UserCorrect 
user1 = User("ABHI",12,"asds@gmsil.com") 
sb= UserCorrect("psql" , "ABHI", "password") 
sb.delete_to_database(user1) 
sb.save_to_database(user1)