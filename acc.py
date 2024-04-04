
def enternum():
    number  = float(input("Please enter a positive number:"))
    while number < 1:
        print("This is not a positive number. Try again")
        number = float(input("Please enter a positive number!!"))
        num = readnum()