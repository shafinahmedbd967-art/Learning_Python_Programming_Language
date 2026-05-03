budget = int (input("Enter your budget: "))
 
# budget 1000 er beshi ba shoman?
if budget >= 1000:
    print("Apni player edition jersey kinte paren")       # False, skip
 
# poroborti check budget ki 700 er beshi 
elif budget >= 700:
    print("Apni fan edition jersey kinte paren")        # True! ei line run hobe
 
# budget aro kom 
else:
    print("Budget baran. Ei budget e player ba fan edition hobe na")       # skip

'''
output:
Enter your budget: 800
Apni fan edition jersey kinte paren
'''