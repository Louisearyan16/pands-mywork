

def displaymenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

# test the function

choice = displaymenu()
print(f"you chose {choice}")