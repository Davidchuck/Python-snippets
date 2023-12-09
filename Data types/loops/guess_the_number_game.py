#This game sets a number and asks the user to guess it. If correct, player wins else if not 
#correct in 3 attempts, player loses.

correct_number=16
guess_count=0
attempts=3

while guess_count < attempts:
    guess=int(input("Guess the Number:"))
    guess_count+=1
    #display remaining attempts
    print("Attempts left:",attempts-guess_count)
  
    if guess==correct_number:
        print("Congratulations! You won!")
        break
    if guess!=correct_number and guess<correct_number:
        print("wrong guess, try again with a higher number")
    elif guess!=correct_number and guess>correct_number:
        print("wrong guess, try again with a lower number")
        
else:
    print("You lose")

    