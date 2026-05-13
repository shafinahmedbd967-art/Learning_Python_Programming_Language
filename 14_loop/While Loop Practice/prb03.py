# Accept a Number and Check It is Palindrome or not

number = int(input("Enter a number: "))
reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if number == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

'''
Enter a number: 12321
output: The number is a palindrome.
Enter a number: 12345
output: The number is not a palindrome.
'''