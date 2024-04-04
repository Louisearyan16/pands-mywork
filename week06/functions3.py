def displaymenu():
    print("what would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice =  input("Type one letter (a/v/q):").strip
    return choice
def doAdd():

    print("in adding")
def doView():
    print("in viewing")


choice = displaymenu()
while (choice !='q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nplease select either a,v ir q")
        choice = displaymenu()

        
