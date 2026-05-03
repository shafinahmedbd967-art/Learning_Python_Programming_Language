age = 20
 
# Normal if-else:
# if age >= 18:
#     result = "Adult"
# else:
#     result = "Minor"
 
# Ek line e same kaj! (ternary operator)
result = "Adult" if age >= 18 else "Minor"
print(result)  # Adult
 
# Ar ekta example: number positive na negative?
num = -5
status = "Positive" if num > 0 else "Negative or Zero"
print(status)  # Negative or Zero
 
# output:
# Adult
# Negative or Zero