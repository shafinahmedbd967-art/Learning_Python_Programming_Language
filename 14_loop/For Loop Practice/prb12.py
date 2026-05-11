# Check String a Palindrome or not using for loop
text = input("Enter a string: ")
reverse_text = ""
for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]
if text == reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# another way:
text = input("Enter a string: ")
reverse_text = text[::-1]
if text == reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''
output: The string is a palindrome.

Enter a string: madam
output: The string is a palindrome.
'''