# Accept a year and check if it is a leap year or not

input = int(input("Enter a year: "))

if (input % 4 == 0 and input % 100 != 0) or (input % 400 == 0):
    print(f"{input} is a leap year.")
else:
    print(f"{input} is not a leap year.")


