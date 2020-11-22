# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapyear = True
        else:
            leapyear = False
    else:
        leapyear = False
    leapyear = True
else:
    leapyear = False

if leapyear == True:
    print("Leap year.")
else:
    print("Not leap year.")
