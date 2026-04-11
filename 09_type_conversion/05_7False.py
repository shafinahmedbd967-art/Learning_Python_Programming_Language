# 0 always False
print(bool(0)) 

# 0.0 o False
print(bool(0.0))

# empty string False
print(bool(""))

# empty list False
print(bool([]))

# empty tuple False
print(bool(()))

# empty dictionary False
print(bool({}))

# None always False
print(bool(None))


"""
output:
False
False
False
False
False
False
"""


"""
Summary: 
0
0.0
""
[]
()
{}
None
are all considered False in Python. Any other value is considered True.
"""