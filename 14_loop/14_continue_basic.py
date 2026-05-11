# continue statement example
# mane jei ste e continue pabo tokhn e abar loop e chole jabo. nicher gula mane jode print ba kono kichu thake 
# oita ar execute hobe na 

for i in range(5):

    # i = 2 hole oi iteration skip hobe
    if i == 2:
        continue

    print(i)

# Output:
# 0
# 1
# 3
# 4