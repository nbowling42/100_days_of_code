import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculate = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    first_number = float(input("What's the first number?: "))

    keep_calculating = True
    while keep_calculating:
        for calculation in calculate:
            print(calculation)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = calculate[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_calculating == "y":
            first_number = result
        elif continue_calculating == "n":
            keep_calculating = False
            calculator()

calculator()