def calculator(a, b, op):
    if op=='+': return a+b
    elif op=='-': return a-b
    elif op=='x': return a*b
    elif op=='/': return a/b
    else:
        print("Invalid input")
        return 0;

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+,-,x,/): ")

print(f'{a} {op} {b} = {calculator(a,b,op)}')