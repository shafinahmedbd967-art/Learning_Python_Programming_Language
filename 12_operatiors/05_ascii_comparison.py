"""
| Character | ASCII Value |
| --------- | ----------- |
| A         | 65          |
| B         | 66          |
| a         | 97          |
| b         | 98          |
| 0         | 48          |
| 1         | 49          |
| Space     | 32          |
| !         | 33          |
| @         | 64          |
| #         | 35          |
| $         | 36          |
| %         | 37          |
| ^         | 94          |
| &         | 38          |
| *         | 42          |
| (         | 40          |
| )         | 41          |
| -         | 45          |
| _         | 95          |
| +         | 43          |
| =         | 61          |
| [         | 91          |
"""

# ASCII comparison example

print("A" < "B")  # A er ASCII value 65, B er ASCII value 66, tai A B theke choto, output hobe True
print("a" < "b")  # a er ASCII value 97, b er ASCII value 98, tai a b theke choto, output hobe True
print("0" < "1")  # 0 er ASCII value 48, 1 er ASCII value 49, tai 0 1 theke choto, output hobe True
print(" " < "!")  # space er ASCII value 32, ! er ASCII value 33, tai space ! theke choto, output hobe True


print("apple" < "banana")  # apple er first character a er ASCII value 97, banana er first character b er ASCII value 98, tai apple banana theke choto, output hobe True
print("Hello" < "hello")  # Hello er first character H er ASCII value 72, hello er first character h er ASCII value 104, tai Hello hello theke choto, output hobe True




print("A" < "a")  # A er ASCII value 65, a er ASCII value 97, tai A a theke choto, output hobe True
print("Python" > "Pyton")  # Python er first character P er ASCII value 80, Pyton er first character P er ASCII value 80, tai Python Pyton theke boro, output hobe True
print("abc" < "abd")  # abc er first character a er ASCII value 97, abd er first character a er ASCII value 97, tai abc abd theke choto, output hobe True



"""
A-Z : 65-90
a-z : 97-122
0-9 : 48-57
Space : 32
"""



# wrong comparison
print("A" < "1")  # A er ASCII value 65, 1 er ASCII value 49, tai A 1 theke boro, output hobe False
# print("A" < 0)  # String ar integer ke compare kora jay na, error hobe, TypeError: '<' not supported between instances of 'str' and 'int'

