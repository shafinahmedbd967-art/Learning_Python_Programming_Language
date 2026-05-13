# The think you accept as input to a function is called parameter. We can pass any type of data as parameter to a function. We can also pass multiple parameters to a
# The thing you provide to a function when you call it is called argument. We can provide any type of data as argument to a function. We can also provide multiple arguments to a function.
def sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

sum(5, 10)  # Positional Argument
sum(45,110) # Argument Change

'''
output: The sum of 5 and 10 is 15
output: The sum of 45 and 110 is 155'''


# parameter example

def greet(name):

    print(f"Hello {name}")

# function call
greet("Shafin")
greet("Python")

# Output:
# Hello Shafin
# Hello Python