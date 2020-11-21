"""A Pythagorean triplet is a set of three
   natural numbers, a < b < c, for which,
      a2 + b2 = c2
   For example, 32 + 42 = 9 + 16 = 25 = 52.
   There exists exactly one Pythagorean triplet
   for which a + b + c = 1000.
   Find the product abc.  """

for a in range(999,1,-1):
   for b in range(999,1,-1):
      for c in range(999,1,-1):
         if(a<b and b<c):
            if(a+b+c == 1000 and a**2+b**2 == c**2 and a+b>c):
               print(a*b*c,a,b,c)

"""ANSWER = 31875000,
   200, 375, 425  """
            
