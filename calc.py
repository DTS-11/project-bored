def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


prompt = input("What do you want to do?\n`add`, `subtract`, `mutliply`, `divide`: ")
operations = ["add", "subtract", "multiply", "divide"]

if prompt not in operations:
    print("Not a valid opertion")

else:
    if prompt == "add":
        resp1 = int(input("Give the first number to add: "))
        resp2 = int(input("Give the second number to add: "))
        result = add(resp1, resp2)
        print(result)

    if prompt == "subtract":
        resp1 = int(input("Give the first number to subtract: "))
        resp2 = int(input("Give the second number to subtract: "))
        result = subtract(resp1, resp2)
        print(result)

    if prompt == "multiply":
        resp1 = int(input("Give the first number to multiply: "))
        resp2 = int(input("Give the second number to multiply: "))
        result = multiply(resp1, resp2)
        print(result)

    if prompt == "divide":
        resp1 = int(input("Give the first number to divide : "))
        resp2 = int(input("Give the second number to divide: "))
        result = divide(resp1, resp2)
        print(result)