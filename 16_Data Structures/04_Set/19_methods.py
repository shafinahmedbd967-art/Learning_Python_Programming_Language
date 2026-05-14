a={1,2,3,4,5,6,7,8,9,10}
b={7,8,9,10,11,12,13,14,15}

#union
union_set = a.union(b)
print(union_set)
# Expected Output:
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

#intersection
intersection_set = a.intersection(b)
print(intersection_set)
# Expected Output:
# {7, 8, 9, 10}

#difference
difference_set = a.difference(b)
print(difference_set)
# Expected Output:
# {1, 2, 3, 4, 5, 6}

# Symmetric difference
symmetric_difference_set = a.symmetric_difference(b)
print(symmetric_difference_set)
# Expected Output:
# {1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15}

# Compound operators
b-=a
print(b)  # difference



# Another Way
print(a|b)  # union
print(a&b)  # intersection
print(a-b)  # difference
print(a^b)  # symmetric difference



