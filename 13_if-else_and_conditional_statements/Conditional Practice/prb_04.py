# Accept name and age of the user and check if the user is valid for voting or not\

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote.")
else:
    print(f"Hello {name}, you are not eligible to vote.")

'''
output:
Enter your name: Shafin 
Enter your age: 22
Hello Shafin, you are eligible to vote.
'''