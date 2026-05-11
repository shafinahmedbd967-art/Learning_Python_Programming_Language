# check whether the number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

'''
output:
Enter a number: 17
17 is a prime number.
'''


# Check prime number with count 
num = int(input("Enter a number: "))
if num > 1:
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

'''
output:
Enter a number: 17
17 is a prime number.
'''