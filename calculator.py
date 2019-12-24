
def simple_calculator(num1, num2, operation):
    if operation.lower() in "*xmultiply":
        result = num1*num2
    elif operation.lower() in "+addplus":
        result = num1+num2
    elif operation.lower() in "/divide":
        result = num1/num2
    elif operation.lower() in "-subtractminus":
        result = num1-num2
    print(str(num1) + " " + operation + " " + str(num2) + " is " + str(result) + ".\n")