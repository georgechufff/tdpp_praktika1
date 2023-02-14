a = int(input())
b = int(input())
choice = input()

operations = {'+' : a + b, '-': a - b, '*': a * b, '/': a / b}

if choice in operations.keys():
	print(operations[choice])
else:
	print("Недопустимая операция")

