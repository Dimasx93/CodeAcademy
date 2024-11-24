#Lesson 12
from random import choice


#Exercise n1
#Script part and to import in modules_12

#Add def
def add(a, b):
    return a+b
#Sub def
def sub(a,b):
    return a-b
#Mult def
def mult(a,b):
    return a*b
#Div def
def div(a,b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

if __name__ == "__main__":

    print("Simple calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Select a number between (1/2/3/4): ")
    num1 = float(input("Select a number: "))
    num2 = float(input("Select a number: "))
    if choice == "1":
        print(f"The addition between {num1} and {num2} is {add(num1,num2)}")
    elif choice == "2":
        print(f"The subtraction between {num1} and {num2} is {sub(num1,num2)}")
    elif choice == "3":
        print(f"The multiplication between {num1} and {num2} is {mult(num1,num2)}")
    elif choice == "4":
        print(f"The division between {num1} and {num2} is {div(num1,num2)}")
    else:
        print("Wrong input.")

#Exercise n2 Three modules

#String def
def string_module(a:str):
    b = a.lower()
    b = b.split()
    return b

#List def
def list_module(a:list):
    return a[::-1]