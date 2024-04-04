# more messing with functions
# flexible arguments




print(1,2,3, end='\t')
print('hi')
# unnamed args
def fun1(*args):
    print(type(args))
    for val in args:
        print(val)

fun1('a','b','c') #other peoples code does have this so good to know



#keyword arguments
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)

fun2(name='joe', age=21, gender='m')

# sample averaage of a few numbers
def ave(*values):
    number_of_values = len(values)
    sum = 0
    for value in values:
        sum+=value

    average = sum /number_of_values
    return average,sum

#print(ave(1,2,3,4,5,6))

average, sumofnum =ave(1,2,3,4,5,6)
print(f"{average}and sum is {sumofnum}")
#ave is a black box, 


