# FInd the greatest elements in a list

numbers = [3, 1, 4, 1, 5, 9]
greatest = numbers[0]
for num in numbers:
    if num > greatest:
        greatest = num
print(f"The greatest element in the list is: {greatest}")

# Output:
# The greatest element in the list is: 9

# another way
l = [3, 1, 4, 1, 5, 9]
largest = l[0]
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
print(f"The largest element in the list is: {largest}")
print(f"The index of the largest element is: {index}")

# Output:
# The largest element in the list is: 9
# The index of the largest element is: 5