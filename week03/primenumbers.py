# generate prime numbers
# check if soemthing is a prime, see if it is divisible by any whole number

#test if can print 2-100
#break-->if do find its not a prime break will allow to jump out of forloop
#algorithm

primes = [] #add as list
upto = 100000
for candidate in range(2, upto):
    #print(candidate) #test first to see if can print 2-100
    isprime = True
    #only need to check if divisble by prime. 
    for divisor in primes:
        #if divisible by an int it is not a prime number
        if(candidate % divisor == 0):
            isprime = False
            #so there is no reason to keep checking
            break
    if isprime:
        primes.append(candidate)

print(primes)

#for loop within a for loop
# will need to look at more complicated code
#put in comments over complicated code
#upto can always change