# while loops


count = 0 
while count <10:
    print("count is", count) #infinite loop (ctrl c to stop it)
    count += 1 # count = count +1


print("at the end count is", count)

count = 10
while count >=0:
    print("countdown", count)
    count -= 1
print("blast off") # make sure to change condition in while loops
 #to get average of data. iterate through data


# sentinal control loops

val= input("type something (q to quit):")
while val != 'q':
    print("Hi Mom")
    val = input("q to quit:")
print("all done")