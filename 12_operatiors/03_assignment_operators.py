# Assignment Operators

"""
| Operator | Meaning           | Example |
| -------- | ----------------- | ------- |
| `=`      | assign value      | x = 5   |
| `+=`     | add & assign      | x += 2  |
| `-=`     | subtract & assign | x -= 2  |
| `*=`     | multiply & assign | x *= 2  |
| `/=`     | divide & assign   | x /= 2  |
| `//=`    | floor divide      | x //= 2 |
| `%=`     | remainder         | x %= 2  |
| `**=`    | power             | x **= 2 |

"""


x = 5     # assign value
print(x)  # output: 5

x += 2    # x = x + 2 er moto kaj kore, x er value 2 diye baray
print(x)  # output: 7

x -= 2    # x = x - 2 er moto kaj kore, x er value 2 diye komay
print(x)  # output: 5

x *= 2    # x = x * 2 er moto kaj kore, x er value 2 diye gun kore
print(x)  # output: 10

x /= 2    # x = x / 2 er moto kaj kore, x er value 2 diye vag kore, division er khetre result hobe float
print(x)  # output: 5.0

x //= 2   # x = x // 2 er moto kaj kore, x er value 2 diye floor division kore, floor division er khetre result hobe float, jodi x er value float hoy
print(x)  # output: 2.0   # floor division er khetre result hobe float, jodi x er value float hoy

x %= 2    # x = x % 2 er moto kaj kore, x er value 2 diye modulo kore, modulo er khetre result hobe float, jodi x er value float hoy
print(x)  # output: 0.0

x **= 2   # x = x ** 2 er moto kaj kore, x er value 2 diye exponentiation kore, exponentiation er khetre result hobe float, jodi x er value float hoy
print(x)  # output: 0.0