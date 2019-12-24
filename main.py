import calculator
import file

try:
    answer = 1
    while answer < 3 and answer > 0:

        answer = int(input("What would you like to do? \n(1) Simple Calculator \n(2) Create / Edit / Read a File \n(3) Nothing \nAnswer: "))

        if answer == 1:
            print("\nYou chose '1'.")
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            operator = input ("What to do with it: ")
            calculator.simple_calculator(num1,num2,operator)

        elif answer == 2:
            print("\nYou chose '2'.")
            option = input("Create, Edit, or Read a file: ")
            if option.lower() == "create":
                file.create_file()
            elif option.lower() == "edit":
                file.edit_file()
            elif option.lower() == "read":
                file.read_file()
            else:
                print("That is not an option.\n")

        else:
            print("\nYou chose '3' or a number that is out of range. Bye.")

except:
    print("\nYou have entered an invalid answer. Bye.")