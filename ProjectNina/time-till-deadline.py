import datetime

user_input=input("Enter your goal with deadline separated by a colon \n")
input_list=user_input.split(":")
goal=input_list[0]
deadline=input_list[1]
deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")

#calculate days from now to deadlinefd
date_today=datetime.datetime.today()

print(deadline - date_today)