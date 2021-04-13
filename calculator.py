# program to make simple calculator using functions
# define the functions

def add(x,y):
    """"This function adds 2 numbers"""
    return x + y

def subtract(x,y):
    """"This function subtracts 2 numbers"""
    return x - y

def multiply(x,y):
    """"This function multiplies 2 numbers"""
    return x * y

def divide(x,y):
    """"This function divides 2 numbers"""
    return x/y

def power(x,y):
    """"This gives power"""
    return pow(x,y)

# take input from user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice =='2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice =='3':
    print(num1, "x", num2, "=", multiply(num1,num2))

elif choice =='4':
    print(num1, "/", num2, "=", divide(num1,num2))

elif choice =='5':
    print(num1, "^", num2, "=", power(num1,num2))

else:
    print("Invalid")
