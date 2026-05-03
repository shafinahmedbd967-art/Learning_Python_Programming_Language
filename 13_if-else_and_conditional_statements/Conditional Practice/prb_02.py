# Accept the gender from user as char and print the respectve greeting message 

gender=input("Enter your gender (m/f): ")

if gender == 'm' or gender == 'M':
    print("Hello Sir!")
elif gender == 'f' or gender == 'F':
    print("Hello Ma'am!")
else:
    print("Invalid gender entered.")

'''
output:
Enter your gender (m/f): m
Hello Sir!
'''