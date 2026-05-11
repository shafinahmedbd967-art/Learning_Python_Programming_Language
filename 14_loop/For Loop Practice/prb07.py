# print a sum of all even & odd number separately from 1 to n
n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers from 1 to {n} is: {even_sum}")
print(f"Sum of odd numbers from 1 to {n} is: {odd_sum}")

'''
output:
Enter a number: 10
Sum of even numbers from 1 to 10 is: 30
Sum of odd numbers from 1 to 10 is: 25
'''