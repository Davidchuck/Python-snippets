#exceptions are meant to handle errors and return customised error messages
#Example 1
try:
    Age=int(input('Enter Age: '))
    Premium=10000
    risk=Premium/Age
    print(risk)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid Input. Please enter a number.")