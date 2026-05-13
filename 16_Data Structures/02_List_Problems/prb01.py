# Print positive and Negative elements from a list


numbers = [1, -2, 3, -4, 5]

for i in numbers:

    if i > 0:
        print(f"{i} is a positive number.")
    elif i < 0:
        print(f"{i} is a negative number.")

# Output:
# 1 is a positive number.
# -2 is a negative number.
# 3 is a positive number.
# -4 is a negative number.
# 5 is a positive number.



# Another way:

l=[1, -2, 3, -4, 5]
print("Positive numbers:")
for i in l:
    if i>0:
        print(i)
print("Negative numbers:")
for i in l:
    if i<0:
        print(i)

# Output:
# Positive numbers:
# 1
# 3
# 5
# Negative numbers:
# -2
# -4