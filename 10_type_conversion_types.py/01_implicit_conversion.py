# implicit type conversion example
# Python automatically datatype change kore\
# Python nijer theke type convert kore
# etake implicit conversion bole

num1 = 10      # integer
num2 = 2.5     # float
num3 = 12      # integer
num4 = 4       # integer

result = num1 + num2   # num1 ke float e convert kore num2 er sathe jog kore result dibe, karon float er precision beshi
vagfol = num3 / num4   # num3 ke float e convert kore num4 er sathe vag kore vagfol dibe, karon division er khetre result hobe float

print(result)          # result er value print kora hocche
print(type(result))    # result er type print kora hocche
print(vagfol)          # vagfol er value print kora hocche
print(type(vagfol))    # vagfol er type print kora hocche   


"""
output:
12.5
<class 'float'>
3.0
<class 'float'>
"""