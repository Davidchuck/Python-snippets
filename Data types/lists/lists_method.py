#append method in lists
#given list
numbers=[2,4,1,0,45,32,54,66]
#to add to list, using append
numbers.append(26)
print(numbers)

#insert a number to a specific position in alist
numbers.insert(0,34) #adds 34 first to the list
print(numbers)

#To remove an item from the list
numbers.remove(66)
print(numbers)

#to clear the list
'''numbers.clear()
print(numbers)''' #returns an empty list

#to remove the last item on a list
numbers.pop() #removes the last item
print(numbers)

#To return position of an item in a list
numbers.index(2) #gives an error if the number is not in the list
print(numbers.index(2))
print(numbers)

#to check availability of a specific number in a list
print (54 in numbers) #returns True if present and false if not

#To check the number of time an item is repeated in a list
numbers.append(2)
print (numbers.count(2))

#append multiple items in alist
fruits=['apple','banana','cherry']

vegetables=['carrot','broccoli','cabbage']
all_items = fruits + vegetables
print(all_items)

#arrange in ascending order
numbers.sort()
#print (numbers)

#Arranges in descending order, Must work with sort
numbers.reverse() 
print (numbers)

#To copy a list
numbers2=numbers.copy()
print(numbers2)
numbers.append(122)
print(numbers)

#remove duplicates from a list
numbers=[34,67,89,12,67]
numbers=list(set(numbers))
print(numbers)

#using loop to remove duplicates
list=[1,1,3,2,4,4,5,6,4,21,34,21,44,21]
uniquelist=[]
for number in list:
    if number not in uniquelist:
        uniquelist.append(number)
print(uniquelist)