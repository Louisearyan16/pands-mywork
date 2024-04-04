# asks user for input and program will tell the user if the number is even or odd


number = int(input("Please enter an integer:"))

if (number % 2) == 0:
        print(f"{number} is an even number")
else:
        print(f"{number} is an odd number")

# a number is odd if it is not evenly divisible by 2, which means we should make use of the % modulo operator. 
# the modulo operator returns the remainder after division, so if something is divisible by 2, with a remainder of 0, it isnt odd. 
# if my number % 2 == 0: means a number is even 
        
# == compares the value or equality of two objects. 