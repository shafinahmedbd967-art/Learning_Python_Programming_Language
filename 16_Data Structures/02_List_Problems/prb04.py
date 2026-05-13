# Find the second largest number in a list.

l = [3, 1, 4, 1, 5, 9]
largest = l[0]
second_largest = l[0]

for i in range(len(l)):
    if l[i] > largest:
        second_largest = largest
        largest = l[i]
    elif l[i] > second_largest and l[i] != largest:
        second_largest = l[i]

print(f"The second largest element in the list is: {second_largest}")

# Output: The second largest element in the list is: 5