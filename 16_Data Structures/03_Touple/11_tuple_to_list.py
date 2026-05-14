# Tuple directly change kora jay na
# Tai list e convert kore modify kora hoy

numbers = (10, 20, 30)

temp = list(numbers)

temp[0] = 100

numbers = tuple(temp)

print(numbers)

# Expected Output:
# (100, 20, 30)