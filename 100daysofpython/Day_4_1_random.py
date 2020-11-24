#Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
coin_toss = random.randint(0,1)

if coin_toss == 1:
    print("Heads.")
elif coin_toss == 0:
    print("Tails.")