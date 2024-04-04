
students = []
def readmodules():
    return []

def doadd(students):
    currentstudent = {}
    currentstudent["name"]=input("enter name:")
    currentstudent["modules"] = readmodules()

    students.append(currentstudent)

    #test
    doadd(students)
    doadd(students)
    print(students)