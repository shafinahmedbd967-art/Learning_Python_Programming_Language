color = "red"
 
# string compare (case-sensitive!)
if color == "red":
    print("Lal rong!")         # True, run hobe
 
elif color == "blue":
    print("Neel rong!")        # skip
 
else:
    print("Onyo rong!")        # skip
 
# user input er sathe (real-world example)
answer = input("Tumi ki student? (hae/na): ")
 
if answer == "hae":
    print("Student discount pabe!")
elif answer == "na":
    print("Full price lagbe!")
else:
    print("Sothik uttor dao: hae ba na")
 
# output (jodi "hae" dei):
# Lal rong!
# Student discount pabe!

# 1 hour 54 minutes pojonto done  