# Check if a string is pallindrome or not using function

def is_pallindrome(text):
    reverse_text = text[::-1]
    return text == reverse_text

# Get user input
user_input = input("Enter a string: ")
# Check if the input string is a palindrome
if is_pallindrome(user_input):
    print("The string is a pallindrome.")
else:
    print("The string is not a pallindrome.")


# another way:
def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev+=st[i]

    if st==rev:
        return "The string is a pallindrome."
    else:
        return "The string is not a pallindrome."
    
pallindrome("madam")
'''
Enter a string: madam
output: The string is a pallindrome.
'''