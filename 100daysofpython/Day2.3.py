# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
years_left = 90 - int(age) 

days_left = int(years_left) * 365
weeks_left = int(years_left) * 52
months_left = int(years_left) * 12


print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
