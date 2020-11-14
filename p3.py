""" The prime factors of 13195 are 5, 7, 13 and 29.
   What is the largest prime factor of the number 600851475143 ? """

a = 600851475143
pr = []
for i in range(2,a//2):
   if a%i == 0:
      pr.append(i)
      print(i)
for j in range(len(pr)):
   for k in range(2,(pr[j]//2)+1):
      if pr[j]%k == 0:
         break
   else:
      new = pr[j]
print(new)

""" answer = 6857 """
