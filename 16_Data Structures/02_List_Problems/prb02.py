# mean of list elements

numbers = [1, 2, 3, 4, 5]

total = sum(numbers)
mean = total / len(numbers)
print(f"The mean of the list is: {mean}")

# Output:
# The mean of the list is: 3.0



# another way
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
mean = total / len(numbers)
print(f"The mean of the list is: {mean}")

# Output:
# The mean of the list is: 3.0
