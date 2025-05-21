# ---Trip Summary---
# Traveler Name : Ali
# Home Town : Peshawar
# Destination : Karachi
# Estimated Cost : 
# Travel ; 10000
# Accommodation : 2000
# other Expenses : 2000
# Total Estimated Cost : 14000
trav_name : str = "Ali" # variable
home_town : str = "Peshawar" 
destination : str = "Karachi" 
trav_cost : int = 10000 
accomod_cost : int = 2000
other_exp : int =2000
tot_cost : int = trav_cost + accomod_cost + other_exp # Arithmetic Operator
print(f"""Traveler Name : {trav_name}       
Home Town : {home_town}
Destination : {destination}
Total Estimated Cost : {tot_cost}""")       # f_String
