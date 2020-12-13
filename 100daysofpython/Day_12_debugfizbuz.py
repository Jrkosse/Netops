## Original Problem. Multiple Bugs
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

for number in range(1, 101):
  # Modified the OR to an AND to correct logic.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # Changed individual ifs to elifs to correct logic. 
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    # Removed brackets to print a number instead of a list
    print(number)