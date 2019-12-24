
def create_file():
    print("You would like to create a file.")
    file = open(input("File name: "), "w")
    file.write(input("Enter content: "))
    file.close()
    print("Done.\n")

def edit_file():
    print("You would like to edit a file.")
    file = open(input("File name: "), "a")
    file.write("\n" + input("What would you like to add to this file? "))
    file.close()
    print("Done.\n")

def read_file():
    print("You would like to read a file.")
    file = open(input("File name: "), "r")
    print(file.read())
    file.close()
    print("Done.\n")