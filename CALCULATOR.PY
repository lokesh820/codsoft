def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y if y!= 0 else "Error: Divison by zero"

while True:
    
    num1 = float(input("Enter first number:"))
    operator = input("Enter operator(+,-,*,/):")
    num2 = float(input("Enter second number:"))
    
    if operator in ['+','-','*','/']:
        result = eval(operator.join([str(num1),str(num2)]))
        print(f"Result:{result}")
    else:
        print("Invalid operator.please enter +,-,*,or/.")
        break
