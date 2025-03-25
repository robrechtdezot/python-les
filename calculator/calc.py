# what do i need?
# input, output, process
# multiple inputs, multiple outputs
# history


def calculator():

    x = input("Enter a number: ")
    y = input("Enter a function symbol: ")
    z = input("Enter another number: ")

    if y == "+":
        print(int(x) + int(z))
    elif y == "-":
        print(int(x) - int(z))
    elif y == "*":
        print(int(x) * int(z))
    elif y == "/":
        print(int(x) / int(z))
    elif y == "%":
        print(int(x) % int(z))
    elif y == "**":
        print(int(x) ** int(z))
    elif y == "//":
        print(int(x) // int(z))
    elif y == "sqrt":
        print(int(x) ** 0.5)
    elif y == "cbrt":
        print(int(x) ** (1/3))
    else:
        print("Invalid function symbol.")

calculator()
while True:
    calculator()
    cont = input("Do you want to perform another calculation? (yes/no): ")
    if cont.lower() != 'yes':
        break
