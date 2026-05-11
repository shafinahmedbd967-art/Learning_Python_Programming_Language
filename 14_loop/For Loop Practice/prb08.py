# print all the factors of a number

n = int(input("Enter a number: "))
print(f"Factors of {n} are: ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')

'''
output:
Enter a number: 12
Factors of 12 are:
1 2 3 4 6 12
'''