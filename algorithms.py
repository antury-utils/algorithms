
def average_two():
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    average = (number1 + number2)/2
    print("Average: {}".format(average))

def get_month():
    months =['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
    month = int(input("Type a number between 1 and 12, to choice a month: "))
    print(months[month-1])

def math_operations():
    number1 = int(input("Operand 1: "))
    operator = input("Operator (+, -, *, /): ")
    number2 = int(input("Operand 2: "))
    result = 0
    if operator == '+':
        result = number1 + number2
    elif  operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2
    print("Result: {} {} {} = {}".format(number1, operator, number2, result))

def greater():
    qty = int(input("How many numbers do you want to compare?: "))
    greater_number = 0
    for i in range(qty):
        number = int(input("Number{}: ".format(i+1)))
        if number > greater_number:
            greater_number = number
    print(greater_number)

def average():
    qty = int(input("Size of samples: "))
    sum = 0
    for i in range(qty):
        sum += int(input("Number{}: ".format(i+1)))    
    print("Average: {}".format(sum/qty))

def greater_age():
    number1 = int(input("Age 1: "))
    number2 = int(input("Age 2: "))
    print("Average age: {}".format(max(number1, number2)))

if __name__ == "__main__":
    while True:
        print("[1] Average 2 numbers")
        print("[2] Get month")
        print("[3] Math Operations")
        print("[4] Greater number")
        print("[5] Average 3 numbers")
        print("[6] Greater age")
        print("[7] Exit")
        option = int(input("Choice an option: "))
        print()
        if option == 1:
            average_two()
        elif option == 2:
            get_month()
        elif option == 3:
            math_operations()
        elif option == 4:
            greater()
        elif option == 5:
            average()
        elif option == 6:
            greater_age()
        elif option == 7:
            exit()
        else:
            print("Wrong option selected, please try again")

