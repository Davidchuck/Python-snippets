name=input("Enter the name: ")
#to count characters of the name
len(name)

if len(name)<3:
    print("name cannot be less than 3 characters")
elif len(name)>50:
    print("Name can only be 50 characters maximum")
else:
    print("Name looks good")