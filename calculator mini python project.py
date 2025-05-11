def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y!=0:
     return x/y
    else:
        return "Error!Division by zero."
def calculator():
    while True:
        print("\nWelcome to my 1st project on python calculator!")
        print("OPERATIONS")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=input("enter choice('1'/'2'/'3'/'4'):")
        if choice=='5':
            print("Thanks for using the calculator.Goodbye!")
            break
        if choice in ('1','2','3','4'):
            try:
                num1=float(input("Enter first number:"))
                num2=float(input("Enter first number:"))
                if choice=='1':
                    print("Result:",add(num1,num2))
                elif choice=='2':
                    print("Result:",sub(num1,num2))
                if choice=='3':
                    print("Result:",mul(num1,num2))
                if choice=='4':
                    print("Result:",div(num1,num2))
            except ValueError:
                    print("invalid input!please select from 1 to 4.")
calculator()
                