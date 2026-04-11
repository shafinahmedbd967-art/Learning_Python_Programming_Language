# Logical operators example
# Logical operators er maddhome amra duita condition ke combine korte pari



"""
AND oeration table  (True = 1, False = 0)
| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |



OR operation table (True = 1, False = 0)
| A     | B     | A or B  |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |


NOT operation table (True = 1, False = 0)
| A     | not A  |
| ----- | ------ |
| True  | False  |
| False | True   |

"""




# and operator example

a = 10

print(a > 5 and a < 20)  # a 5 theke boro and a 20 theke choto kina check kore, output hobe True
print(a > 5 and a < 15)  # a 5 theke boro and a 15 theke choto kina check kore, output hobe True
print(a > 5 and a < 10)  # a 5 theke boro and a 10 theke choto kina check kore, output hobe False
print(a > 15 and a < 20) # a 15 theke boro and a 20 theke choto kina check kore, output hobe False

print(a > 5 or a < 10)   # a 5 theke boro or a 10 theke choto kina check kore, output hobe True
print(a > 15 or a < 10)  # a 15 theke boro or a 10 theke choto kina check kore, output hobe False
print(a > 15 or a < 20)  # a 15 theke boro or a 20 theke choto kina check kore, output hobe True

print(not a > 5)         # a 5 theke boro na kina check kore, output hobe False
print(not a < 5)         # a 5 theke choto na kina check kore, output hobe True


# age eligibility example

age = 20

print(age >= 18 and age <= 60)   # age 18 theke boro or equal and age 60 theke choto or equal kina check kore, output hobe True

a = 10

print((a > 5 and a < 15) or a == 100)  # a 5 theke boro and a 15 theke choto kina check kore, or a 100 er soman kina check kore, output hobe True


