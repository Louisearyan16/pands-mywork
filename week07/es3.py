

import sys


if len(sys.argv) != 2:
    print("please enter python es.py mobydick.txt")
    sys.exit(1)

filename = sys.argv[1]

if not filename.endswith('txt'):
        print('Not a txt file!')


try:
    with open(filename, 'r') as f:
        content = f.read()
        number_of_es = content.count('e')
        print(number_of_es)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

