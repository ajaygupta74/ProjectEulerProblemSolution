"""A palindromic number reads the same both ways. The largest
   palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
   Find the largest palindrome made from the product of two 3-digit numbers. """

import math
li = []
for i in range(999,100,-1):
   for j in range(999,100,-1):
      n = str(i*j)
      num = n[::-1]    #reversing the product
      if (num == n):       #checking if palidrome
         if int(num) > 10000:       # to finding large
            li.append(int(num))

print(max(li))    finding largest palidrome

"""answer =  906609 """


         
