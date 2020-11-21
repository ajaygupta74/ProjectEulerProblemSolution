"""The sum of the squares of the first ten natural numbers is, 385
   The square of the sum of the first ten natural numbers is, 3025
   Hence the difference between the sum of the squares of the first
   ten natural numbers and the square of the sum is .2640
   Find the difference between the sum of the squares of the first
   one hundred natural numbers and the square of the sum.   """

nsum = 0
ssum = 0
for i in range(1,101):
   nsum = nsum + i**2
   ssum = ssum+i
print(nsum,ssum**2,"deff = ",ssum**2-nsum)

"""answer = 25164150"""

