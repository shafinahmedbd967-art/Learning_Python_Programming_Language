# Question: Write a program that takes the temperature as input and categorizes it as follows:
# - Above 40: "It's a very hot day."
# - Above 30: "It's a hot day."
# - Above 20: "It's a pleasant day."
# - Above 10: "It's a cool day."
# - Above 0: "It's a cold day."
# - 0 or below: "It's a freezing day."


temparature= int(input("Enter the temparature: "))

if temparature > 40:
    print("It's a very hot day.")
elif temparature > 30:
    print("It's a hot day.")
elif temparature > 20:
    print("It's a pleasant day.") 
elif temparature > 10:
    print("It's a cool day.")
elif temparature > 0:
    print("It's a cold day.")
else:
    print("It's a freezing day.")
