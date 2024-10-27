# IMPORTS
import math

# GLOBAL VARIABLE DEFINITIONS
current_result = 0
num_calcs = 0
total = 0


# PROMPT USER FUNCTION
def menu():
    # print current result
    print(f"Current Result: {round(current_result,2)}")
    print()
    print("Calculator Menu\n---------------")
    print("0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication")
    print("4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average")
    print()


# first prompt before entering loop
menu()
while True:  # always true --> break to exit
    # variables for each instance of a calculator
    selection = int(input("Enter Menu Selection: "))

    if selection not in range(8):
        print("Error: Invalid selection!")
        print()
        continue

    if selection == 0:  # exit program condition
        print("Thanks for using this calculator. Goodbye!")
        break

    elif selection == 7:  # exit program condition
        if num_calcs == 0:  # condition for no calculations
            print("Error: no calculations yet to average!")
        else:
            # display average
            print(f"Sum of calculations: {total}")
            print(f"Number of calculations: {num_calcs}")
            print(f"Average of calculations: {total/num_calcs:.2f}")

        print()  # spacing newline
        continue  # go directly to next prompt without displaying menu

    else:
        # actually do calculations now
        operand_1 = float(input("Enter first operand: "))
        operand_2 = float(input("Enter second operand: "))
        if selection == 1:
            # addition
            add = lambda op1, op2: op1 + op2
            current_result = add(operand_1, operand_2)

        elif selection == 2:
            # subtraction
            current_result = operand_1 - operand_2

        elif selection == 3:
            # multiplication
            current_result = operand_1 * operand_2

        elif selection == 4:
            # division
            current_result = operand_1 / operand_2

        elif selection == 5:
            # exponentiation
            current_result = operand_2 ** operand_1

        elif selection == 6:
            # logarithm
            current_result = math.log(operand_2, operand_1)

        # contribute to statistics/average
        num_calcs += 1
        total += current_result

        # print()     # print newline regardless of selection to provide spacing for next prompt
        menu()      # print menu again




