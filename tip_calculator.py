#Welcome message
print("Hi! Welcome to the Tip Calculator." "\n")

total_bill = float(input("What was the total bill? $")) 

tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15?" "\n"))

total_people = int(input("How many people are splitting this bill?" "\n"))

print (f"Each person should should pay: ${round(total_bill / total_people * (tip_percent/100), 2)}" "\n")
  
