daily_dose=4
cost_pertab=1799.65
days_in_ayear=365
patient1_age=78
patient2_age=12
life_expectation=90

#calculate cost of medicines to be inccured for each patient by the time they die at 90 years
def calculate_medicine_cost(patient_age, life_expectation):
    years_left = life_expectation - patient_age
    total_cost = (years_left * days_in_ayear) * cost_pertab * daily_dose
    return total_cost

#print the cost
print("The estimated cost of medicine for Patient 1 is: ksh", calculate_medicine_cost(patient1_age, life_expectation ))

print("The estimated cost of medicine for Patient 2 is: ksh", calculate_medicine_cost(patient2_age, life_expectation ))