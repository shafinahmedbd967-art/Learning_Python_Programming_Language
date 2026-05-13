# Count all letters, digits, Special characters in a string

text = input("Enter a string: ")

letters = 0
digits = 0
special_characters = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        special_characters += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Characters:", special_characters)

'''
Enter a string: Hello World! 123
output: Letters: 10
Digits: 3
Special Characters: 2
'''

