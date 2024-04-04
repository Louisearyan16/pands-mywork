
# reads in a st5ring and strips any leading or trailing spaces
# it also converts all the letters to lower case
# it then ouputs the lengths of the original string and the normalised one

rawstring = input("Please enter a string")
normalisedstring = rawstring.strip().lower()

lengthofrawstring  = len(rawstring)
lengthofnormalisedstring = len(normalisedstring)

print(f"That string normalised is:{normalisedstring}")
print(f"we reduced the input string from {lengthofrawstring} to {lengthofnormalisedstring} characters.")

