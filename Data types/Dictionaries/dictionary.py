#Defining a dictionary
CustomerDetails={
    "Name":"John Doe",
    "Age":30,
    "Phone":92330903,
    "Email":"john.doe@gmail.com"
}
#Accessing the value of Name using its key in the dictionary
print("Customer Name is", CustomerDetails["Name"])
#Changing the value of Age to 31 and accessing it again
CustomerDetails["Age"]=31
#print("Customer Age is now", CustomerDetails["Age"]) #Returns an error if value is not in dictionary

#Accessing values using get()
print(CustomerDetails.get("nanan")) #Returns None if value is not in the dictionary