# anonymous functions

#x = lambda arg: arg ** 2
#answer = x(4)
#print(answer)

businesstype = 'standard'
businesstype = 'reduced'

vatcalc = lambda amount: amount*0.23
if businesstype =='standard':
    vatcalc =lambda amount:amount*0.135

cash = 10
print(vatcalc(cash))

#sort a list
numbers = [2,33,55,1,4]
sortednumbers = sorted(numbers)
print(f"{numbers}sorted is {sortednumbers}")

# sort a dictionary
data = [{'first':'guido', 'last':'van rossum', 'YOB':1956},
        {'first': 'grace', 'last':'hopper', 'YOB':1906},
        {'first':'alan','last':'turing', 'YOB':1912}]


sorteddata = sorted(data, key=lambda x: x['last'])
#print(f'{data} sorted is {sorteddata}')
for item in sorteddata:
    print(item)