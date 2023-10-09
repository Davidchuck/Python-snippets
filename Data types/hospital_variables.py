#variables to store details of a patient and show whether he/she is new or not
patient_name="John Smith"
patient_age=20
isnew = False  #True for New Patient, False otherwise.
print(type(isnew))

print("The patient\'s name is: ", patient_name, "He is ", patient_age, "years old and")
#print is new if isnew=true
if isnew:
    print(patient_name, "Is a new patient")
else:
    print("Patient",patient_name,"has already been seen before.")

