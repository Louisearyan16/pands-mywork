
# accounts.py
# This program reads in a 10 character account number and outputs the number with only the last 4 digits showing. 
# Author: Louise Ryan

numberentered = False

while numberentered == False:      # while loop
    accountnumber = input("Please enter a 10 digit account number: ")  # Reads in a 10 digit number from the user
    if len(accountnumber) == 10:      # if else checks if the correct number of digits are entered  
                                       
         newaccountnumber = "x" *6 + accountnumber[-4:] 
          # "x"*6 hides the first six characters 
          # accountnumber[-4:] takes last 4 characters out of string
         
         print("Your account number is", newaccountnumber)
         numberentered = True     
    else: 
               print("Error!")
         
       
# modifed code to deal with account numbers of any length

numberentered = False

while numberentered == False: 
    accountnumber = input("Please enter an account number: ")
    if accountnumber.isdigit(): 
        newaccountnumber = "x" * (len(accountnumber)-4) + accountnumber[-4:] 
        numberentered = True   
    else:
        print("Error!")
