import sys


if len(sys.argv) != 2:
    print("python es.py mobydick.txt")
    sys.exit(1)

filename = sys.argv[1]


try:
    with open(filename, 'r') as f:
        content = f.read()
        number_of_es = content.count('e')
        print(number_of_es)
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

    
