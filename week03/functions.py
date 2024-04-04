
#x, y, z =1,2,3
#print(x,y,z,sep ='',end='')
#print(f"{x}-{y}-{z}")
#print("{} {} --{}".format(x,y,z)) # dont use it 

def topower(number, power=3):
    #print(number)
    return(number ** power)


#ans = cube(23)
#print(f" we got {ans}")

#print(f"and 33 is {cube(33)}")
num = 45
print(f"and {num} is {topower(num,3)}") # can change power but will default to 3 if no argument added
