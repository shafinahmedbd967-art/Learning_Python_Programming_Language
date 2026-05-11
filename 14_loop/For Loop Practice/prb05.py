# sum upto n terms 
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of first {n} natural numbers is: {sum}")

'''
output:
Enter a number: 10
Sum of first 10 natural numbers is: 55
Enter a number: 5
Sum of first 5 natural numbers is: 15
'''