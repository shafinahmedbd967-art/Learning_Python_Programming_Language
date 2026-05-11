# negative number skip

numbers = [5, -2, 8, -1, 10]

for num in numbers:

    if num < 0:
        continue

    print(num)

# Output:
# 5
# 8
# 10