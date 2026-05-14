# Indexing diye specific value access kora hoy

colors = ("red", "green", "blue")

print(colors[0])
print(colors[1])
print(colors[2])

# Negative indexing
print(colors[-1])

# Expected Output:
# red
# green
# blue
# blue

# Another way:
a= ("red", "green", "blue", 1,2,3,4,5,print(), [1,2,3], (1,2,3))
index= a.index(5)
print(index)

# Expected Output:
# 7
