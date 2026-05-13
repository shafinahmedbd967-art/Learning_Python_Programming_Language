# Types of Arguments in Python

# Positional Argument: 
# The most common type of argument is the positional argument. 
# In this type of argument, the values are passed to the function in the same order as the parameters are defined in the function. 
# The first value is assigned to the first parameter, the second value is assigned to the second parameter, and so on.

from unicodedata import name


def sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

sum(5, 10)  # Positional Argument
sum(45,110) # Argument Change

'''
output: The sum of 5 and 10 is 15
output: The sum of 45 and 110 is 155
'''


# Default Argument:
# In this type of argument, we can provide a default value for a parameter. 
# If the caller does not provide a value for that parameter, the default value will be used

def hello(name,age):
    print(f"Hello {name}, you are {age} years old.")

hello("Shafin", 22)  # Output: Hello Shafin, you are 22 years old.
hello(22,"Shafin")   # Output: Hello 22, you are Shafin years old. (Argument Change)

# better option (keywrord argument)
hello(name="Shafin", age=22) # Output: Hello Shafin, you are 22 years old.
# This is known as keyword argument, where we specify the parameter name along with the value.


