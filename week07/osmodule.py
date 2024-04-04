# messing with the os module

import os

FILENAME = "files.py"

if os.path.exists(FILENAME):
    with open(FILENAME, 'r') as f:
        for line in f:
            print(line, end = '')
else:
    print(FILENAME, 'does not exist')
# make sure in right directory
    
os.remove('data2.txt')  #to remove file 


