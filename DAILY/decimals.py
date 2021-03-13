# expecting 0 but result is weird due to precision so not accurate

x = .10 + .10 + .10 - .30
print('x is {}'.format(x))



#-------------------------SOLUTION FOR ABOVE PROBLEM------------------------

from decimal import Decimal

a = Decimal(".10")
b = Decimal(".30")

x = a + a + a - b

print('x is {}'.format(x))