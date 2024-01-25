#ask user to input phone Number
phone=input("Please enter Phone No: ")

#convert the entered phone to word
phoneDictionary={
   "0":"Zero","1":"one","2":"two",
   "3":"three","4":"four","5":"five",
   "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"
}
Output=""
for number in phone:
    Output += phoneDictionary.get(number, "!") + " "
print("Phone Number is ", Output)


