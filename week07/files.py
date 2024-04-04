# messing with files

FILENAME = "data.txt"
# can only read in certain parts of file at one time if file is too large may hit a buffer
'''
with open(FILENAME, 'r') as f:
     for data in f:
        #print(data, end = '') printing out all the data in the file. 
       # print(data.strip())      stripping out some of the characters and putting in a new line in in the print  # to take out spaces between lines
        print(data[:-1])
'''
# data2 did not exist. created it, check ls. look inside data2.txt-->cat /\data2.txt
with open('data2.txt', 'w+') as f:
    f.write('how now\n')  #\n-->new line
    f.write('brown cow')
    f.seek(0) # beginning of file byte 0 
    data =f.read()
    print(data)



print('done')




