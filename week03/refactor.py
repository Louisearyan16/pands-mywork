# read in two numbers and multiply them


def readnum(message = 'enter number:'):
    num = False
    while(num==False):
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number, try again", end ='')
    return num

num1 = readnum()
num2 = readnum("enter num2")

answer = num1 * num2
print(f"answer is {answer}")


