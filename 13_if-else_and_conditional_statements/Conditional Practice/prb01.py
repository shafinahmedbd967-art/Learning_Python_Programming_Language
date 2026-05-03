# Accept two numbers and print the larger one

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
'''
output:
Enter first number: 10
Enter second number: 20
20.0 is greater than 10.0
'''