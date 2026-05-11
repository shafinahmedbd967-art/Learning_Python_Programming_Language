# Accept a number and check if it is a perfect number or not


n = int(input("Enter a number: "))
sum_of_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i

if sum_of_factors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")