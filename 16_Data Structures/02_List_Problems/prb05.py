# Check if list is sorted or not

a= [1, 2, 3, 4, 5]
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("The list is not sorted.")
        break
else:
    print("The list is sorted.")

# Output:
# The list is sorted.