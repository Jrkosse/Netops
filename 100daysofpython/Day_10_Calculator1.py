from Day_10_Calculator1_art import logo

def add(n1, n2):
  return n1+n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(logo)

    n1 = float(input("What is the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        op = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        calculation_function = operations[op]
        answer = calculation_function(n1,n2)
        print(f"{n1} {op} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calc: ") == 'y':
            n1 = answer
        else:
            should_continue = False
            calculator()

calculator()


