import random
mylist=[]

def Random():
  for i in range(5):
     eded_random=random.randint(20,50)
     mylist.append(eded_random)
  return mylist

print(Random())

import math
cutlist=[]

for i in mylist:
   if i%2==0:
      a=int(math.pow(i,2))
      cutlist.append(a)  
   else:
       pass
    
print(cutlist)