#given a list of all items in a room
'''names=['Table','Chair','Desk','Laptop','Speakers']
names[0]='Tables' #changes the value of the 1st index to Tables
print(names) #returns all
print(names[3])
print(names[2:4])'''

#List that returns the larget number
numbers=[5,8,9,7,6,4,2,1,3,20]
'''largest_num = max(numbers)
print("The largest number is ",largest_num)'''
#assume the first number is th largest
max=numbers[0]
#Iterate to compare the other numbers and reset the max number
for n in numbers:
    if n>max:
        max=n
print('The largest number is ',max)