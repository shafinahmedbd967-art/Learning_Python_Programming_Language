# Separate each digit of a number and print them on the new line


number = int(input("Enter a number: "))
while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10     # Float division to remove the last digit

'''
Enter a number: 12345
output:
5
4
3
2
1
'''