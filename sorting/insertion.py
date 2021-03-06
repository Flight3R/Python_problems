#from random import *
from time import *

def insertionsort(A,ln):
  for i in range(1,ln):
    x = A[i]
    j = i-1
    while j >= 0 and A[j] > x:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = x
 

# a = list(range(10))
# shuffle(a)
# start=time()
# insertionsort(a,len(a))
# print(str(time()-start))
# print(a)