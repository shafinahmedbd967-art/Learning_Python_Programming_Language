# Accept a year and check if it is a leap year or not

input = int(input("Enter a year: "))

if (input % 100 == 0 and input % 400 == 0):
    print(f"{input} is a leap year.")
elif (input % 100 != 0 and input % 4 == 0):
    print(f"{input} is a leap year.")
else:
    print(f"{input} is not a leap year.")

'''
output:
Enter a year: 2020
2020 is a leap year.
'''
