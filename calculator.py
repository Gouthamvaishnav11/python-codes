def add(num1, num2):
    return num1 + num2

def multiple(num1, num2):
    return num1 * num2

def sub(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

while True:
    print("__________Simple Calculator___________")
    print("1. Add")
    print("2. Multiple")
    print("3. Subtract")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("The calculation is exited. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result:" , add(num1,num2))
        if choice =="2":
            print("Result: ",multiple(num1,num2))
        if choice == "3":
            print("Result:" , sub(num1,num2))
        if choice == "4":
            print("Result:" , divide(num1,num2))
        if choice =="5":
           print("Result:" , modulo(num1,num2))
        else:
            print("the valid number is  correct pls enter correct number.")
