age = int(input("Enter your age: "))
has_ticket = int(input("Do you have a ticket? (1 for Yes, 0 for No): "))
 
# AND: duita condition-i True hote hobe
if age < 18 and not has_ticket:
    print("Apnar boyosh hoy nai,ticket o nai !")      # False and True = False, skip
 
elif age >= 18 and not has_ticket:
    print("Apni ticket chara concert e jete parben na")  # True and False = False, skip
elif age < 18 and has_ticket:
    print("Apni concert e jete parben na, karon apni 18 er nicher")  # False and True = False, skip
else:
    print("Apni concert e jete parben karon apni 18 er upore and ticket ache")  # True and True = True, run hobe