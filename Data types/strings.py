#Handling differnt types of strings
course='Python course for begginers'
print(course)

course2='Python course for "beginners "'
course3="Python course for \"beginners\" "
print (course2)
print ("\n") #new line
print(course3, "\n")  


#printing multiple line string
email='''
Hello Team

Your issue was resolved.
Please check to confirm

Regards,
Tech support Team

'''
print(email)


#String Indexing
course="This is python"
new_course=course
print(course[1:-1])
print(new_course)
