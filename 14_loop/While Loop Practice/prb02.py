# Accept a Number and Print  it Reverse

number= int(input("Enter a number: "))
reverse= 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10     # Float division to remove the last digit

print("Reverse of the number is:", reverse)


'''
Enter a number: 12345
output: Reverse of the number is: 54321
'''