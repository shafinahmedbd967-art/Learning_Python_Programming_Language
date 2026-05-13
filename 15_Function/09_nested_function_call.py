# function calling another function

def hello():

    print("Hello")

def world():

    hello()
    print("World")

world()

# Output:
# Hello
# World