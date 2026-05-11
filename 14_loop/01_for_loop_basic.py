# for loop basic example 
# print 1 to 20 numbers using for loop  


a= range (1,21,1)   # range(start, stop, step) used to generate a sequence of numbers

for i in a:   # for loop er syntax: for variable in sequence:
    print(i)

'''
output:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''


# range directly o loop er vitor use kora jay, alada variable declare kora lagbe na
for i in range(1,21,1):
    print(i)
'''
output:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''


# range e defauult vabe  kora jay, jodi step 1 hoy, tahole step er value dewa lagbe na
# initial value hobe 0, tai start er value dewa lagbe na
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4