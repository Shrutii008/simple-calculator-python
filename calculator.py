# Simple Console Calculator
# Python Project by Shruti Verma
# Features: Add, Subtract, Multiply, Divide,Loop until exit, Division by zero check 

while True:
    print("\n--- Simple Calculator ---")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break  # Stop the loop

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice. Please try again.")