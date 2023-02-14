a = int(input())
b = int(input())
choice = input()

operations = {'+' : a + b, '-': a - b, '*': a * b, '/': a / b}

print(operations[choice] if choice in operations.keys() else "Недопустимая операция")
