li = []
i = 1
while i >0:
   for j in range(1,):
      for k in range(1,i//2):
         if j%k == 0:
            break;
         else:
            li.append(j)
   if(len(li)>6):
      break
print(li)
