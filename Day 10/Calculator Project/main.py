from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    calculating = True
    result = 0
    n1 = float(input("What's the first number?:"))
    while calculating:
        for i in operations:
            print(i)
        operation = input("Pick an operation: ")

        n2 = float(input("What's the next number?:"))
        if operation in operations:
            result = operations[operation](n1, n2)
        else:
            print("Wrong operation")

        print(f"{n1} {operation} {n2} = {result}")
        keep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if keep == 'yes' or keep == 'y':
            n1 = result
        else:
            result = 0
            calculating = False
            calculator()

calculator()