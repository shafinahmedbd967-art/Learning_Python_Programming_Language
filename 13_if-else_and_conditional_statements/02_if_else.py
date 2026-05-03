age = int(input("Enter your age: "))
 
# condition check: age 18 er beshi ba shoman?
if age >= 18:
    print("Tumi Vote Dite Paro!")      # Age >= 18, tai ei line skip hobe
else:
    print("Tumi Vote Dite Paro Na!")   # Age < 18, tai ei line run hobe
 
'''
output:
Enter your age: 20
Tumi Vote Dite Paro!
'''