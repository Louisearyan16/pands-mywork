# for loops 


#for elim in list
    #do something

# for number in range(1,10)
    #do something


boats = ['sigma', 'x yacht', 'swan']
for boat in boats:
    print("id rather be out in a ", boat, sep ="", end="\n") # comma put in an extra space.

for i in range (1,10):# index. used to store the value of the current iteration of a loop
    print(i)
print("all done i is now",i)

if "swan" in boats:
    print("that is a boat")