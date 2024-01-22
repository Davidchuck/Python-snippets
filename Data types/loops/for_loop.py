#Iterates over a collection wg of a string or array.
#The function takes two parameters:
#example
'''for item in 'python':
    print(item) #prints p,y,t,h,o,n,

#Examplle 2
    for item in ['car','bike','scooter']:
        print(item)
#Example3
    for item in range(1,10):
        print(item)'''

#calculate total cost of items in for loop
prices=[10,20,30]  
total=0
for price in prices:
    total+=price
print(f"Total cost {total}")