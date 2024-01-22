#Nested for loop to print cordinates
'''for x in range (4):
    for y in range(3):
        print (f'({x}, {y})')
        '''
#print number of x per loop of numbers
numbers=[1,1,1,1,5]
for x in numbers: 
    count=''
    for y in range(x):
        count +='x'  
    print(count)
    
