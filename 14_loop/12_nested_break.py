# nested loop break example

for i in range(3):

    for j in range(3):

        if j == 2:
            break

        print(i, j)

# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1