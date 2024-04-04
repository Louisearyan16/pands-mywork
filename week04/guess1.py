# prompts user to guess a number
# program should keep prompting the user to guess the number until the user gets the right one

numbertoguess = 30
guess = int(input("Please guess the number:"))
while guess != numbertoguess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numbertoguess)