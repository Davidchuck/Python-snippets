x='help'
y='start'
z='stop'
v='quit'
started=False
print("Enter your command, help, start, stop or Quit \n")
command=""
while command !='quit':
    command=input("> ").lower()
#while command==x:
    if command==x:
        print("enter Start to start the car \n Stop to stop the car \n Quit to end the game")
    if command==y:
        if started:
            print("The car is already started!")
        else:
            started=True
            print("Car Started ... Ready to go!")
    if command==z:
        if not started:
            print("The car is already Stopped!")
        else:
            started=False        
            print("Car Stopped!")
    elif command==v:
        break    
else:
  print("I do not understand you")
