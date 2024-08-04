def sumNumbers(a, b):
    return a + b
def subNumbers(a, b):
    return a - b
def multNumbers(a, b):
    return  a * b
def divNumbers(a, b):
    return a / b
def organization(operation, operadors, d):
    operation = operation.replace(" ", "")

    for operador in operadors:
        if operador in operation:
            a, b = operation.split(operador)
            if a == '':
                a = d
                b = int(b)
            else:
                a = int(a)
                b = int(b)

    if '+' in operation:
        c = sumNumbers(a, b)
        return c
    elif '-' in operation:
        c = subNumbers(a, b)
        return c
    elif '*' in operation:
        c = multNumbers(a, b)
        return c
    elif '/' in operation:
        c = divNumbers(a, b)
        return c

operadors = ['+', '-', '*', '/']
d = 0

while True:
    operation = input()
    d = organization(operation, operadors, d)
    print(d)