print("Welcome to Calculator Application Running as a container")

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
while True:
    print("Enter Any Two number to perform Add/Sub/Mul/Div")
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the Second Number: "))
    print("Select from below options to perform :")
    print("1 : Addition")
    print("2 : Subtraction")
    print("3 : Multiplication")
    print("4 : Division")
    testInput = int(input("Enter the Option from above displayed field: "))

    if(testInput == 1):
        result = add(num1,num2)
        print("sum of %d + %d = %d" %(num1,num2,result))
    elif(testInput == 2):
        result = sub(num1,num2)
        print("Substrcation  of %d - %d = %d" %(num1,num2,result))
    elif(testInput == 3):
        result = mul(num1,num2)
        print("Multiplication of %d * %d = %d" %(num1,num2,result))
    elif(testInput == 4):
        result = div(num1,num2)
        print("Division of %d / %d = %d" %(num1,num2,result))
    else:
        print("the Entered input is invalid select from the below options")