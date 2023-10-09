weight=int(input("Enter weight: "))
units= input("in L(lbs) or K(Kgs)?")

if units.upper()=='L':
    weight_inKg=weight*0.453592
    print(f"You are: {weight_inKg}Kgs")
elif units.upper()=='K':
    weight_inlb=weight/0.453592
    print(f"You are: {weight_inlb}pounds")
else:
    print("Invalid units inputs")