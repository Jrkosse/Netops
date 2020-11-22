#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip_percent = input("What is the tip percent? 10,12,15?")
num_people = input("How many people to split the bill with? ")


tip_amount = float(bill) * (int(tip_percent) / 100)
total_bill = float(bill) + tip_amount 
bill_per_person = total_bill / int(num_people)

print(f"Each person should pay: {str(round(bill_per_person,2))}")