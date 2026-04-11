"""
OPerator precedence  (BODMAS)

| Order | Meaning            |
| ----- | ------------------ |
| B     | Brackets `()`      |
| O     | Power `**`         |
| D     | Division `/ //`    |
| M     | Multiplication `*` |
| A     | Addition `+`       |
| S     | Subtraction `-`    |

"""


# operator precedence example

result = 10 + 5 * 2

print(result)   # protome multiplication hobe, tarpor addition hobe, karon multiplication er precedence beshi

"""
output:
20   
"""


result = (10 + 5) * 2

print(result)  # protome brackets er moddhe calculation hobe, tarpor multiplication hobe, karon brackets er precedence beshi

"""
output:
30
"""



result = 10 + 5 * 2 ** 2   # protome exponentiation hobe, tarpor multiplication hobe, tarpor addition hobe, karon exponentiation er precedence beshi, tarpor multiplication er precedence beshi

print(result)  # output: 30

"""
output:
30
"""



result = 20 / 2 * 5

print(result) # protome division hobe, tarpor multiplication hobe, karon division o multiplication er precedence same, tai left to right order e calculation hobe

"""
output:
50.0
"""



result = (2 + 3) * 4 ** 2 / 2 # protome brackets er moddhe calculation hobe, tarpor exponentiation hobe, tarpor multiplication hobe, tarpor division hobe, karon brackets er precedence beshi, tarpor exponentiation er precedence beshi, tarpor multiplication o division er precedence same, tai left to right order e calculation hobe

print(result) 

"""
output:
50.0
"""