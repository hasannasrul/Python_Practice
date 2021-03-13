# upper , lower ,number , symbol identifier 
import re

inp = input()
first = inp[0]

lower = re.findall("[a-z]",first)
upper = re.findall("[A-Z]",first)
number = re.findall("[0-9]",first)
special = re.findall("[+]",first)

if lower:
    print("Lower")
elif upper:
    print("Upper")
elif number:
    print("Number")
else:
    print("Special")

