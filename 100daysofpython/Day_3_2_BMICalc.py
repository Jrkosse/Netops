# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# Start - Calculate the BMI
height_sq = float(height) ** 2
bmi = round(int(weight) / height_sq)

# Nested IF statements. Meh
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5:
    if bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi > 25:
        if bmi < 30:
            print(f"Your BMI is {bmi}, you are slightly overweight.")     
        elif bmi > 30:
            if bmi < 35:
                print(f"Your BMI is {bmi}, you are obese.")
            if bmi > 35:
                print(f"Your BMI is {bmi}, you are clinically obese.")

