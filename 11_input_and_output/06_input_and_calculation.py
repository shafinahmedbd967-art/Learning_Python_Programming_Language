# user theke number input niye calculation way 1 

num1 = input("Enter first number: ")  # user theke first number input ney as string
num2 = input("Enter second number: ")  # user theke second number input ney as string


print(type(num1))  # num1 er type print kore, input() diye number input nile se string e ashe
print(type(num2))  # num2 er type print kore, input() diye number input nile se string e ashe


total = int(num1) + int(num2)   # input() diye number input nile se string e ashe, tai string ke integer e convert kore addition kora hoy

print("Total =", total)         # total er value print kore
print(type(total))           # total er type print kore, total er type hobe integer



"""
output:
Enter first number: 10
Enter second number: 20
<class 'str'>
<class 'str'>
Total = 30
<class 'int'>
"""



# user theke number input niye calculation way 2

num3 = int(input("Enter first number: "))  # user theke first number input ney and string ke integer e convert kore
num4 = int(input("Enter second number: "))  # user theke second number input ney and string ke integer e convert kore


print(type(num3))  # num1 er type print kore, input() diye number input nile se string e ashe
print(type(num4))  # num2 er type print kore, input() diye number input nile se string e ashe


total2 = num3 + num4  # already converted to integers, so direct addition

print("Total =", total2)  # total er value print kore
print(type(total2))  # total er type print kore, total er type hobe integer


"""
output:
Enter first number: 15
Enter second number: 25
<class 'int'>
<class 'int'>
Total = 40
<class 'int'>
"""
