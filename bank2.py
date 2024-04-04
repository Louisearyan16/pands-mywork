# bank.py
# This program reads in two money amounts (in cent) and prints out the sum of these in euro with the decimal point between the euro and cent of the amount.
# Author: Louise Ryan

import decimal

x = int(input('Enter amount 1:(in cent)'))
y = int(input('Enter amount 2:(in cent)'))
sum = (x + y)
sum1 = (sum)//100
sum2 = (sum) % 100

a = sum1
b = sum2
a1 = str(a) + '.' + str(b)
print(a1)

print(f"The sum of these is €{a1}")

