# 100 Days of Python!
# Jeremy Kosse
# 11/25/2020
# Day 2: Understanding Data types and how to manipulate strings

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

# Start
height_sq = float(height) ** 2
bmi = int(int(weight) / height_sq)
print(int(bmi))
