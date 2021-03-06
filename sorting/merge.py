#from random import *

def merge(A, a, c, b):
  C = A[a:b+1]
  sr=c-a
  ko=b-a
  i=0
  j=sr+1
  k=a
  while i <= sr and j <= ko:
    if C[i] < C[j]:
      A[k] = C[i]
      i+=1
    else:
      A[k] = C[j]
      j+=1
    k+=1
  if i<=sr:
    A[k:b+1] = C[i:sr+1]
  else:
    A[k:b+1] = C[j:]
 
    
def mergesort(A, a, b):
  if a < b:
    c = (a + b)//2
    mergesort(A, a, c)
    mergesort(A, c+1, b)
    merge(A, a, c, b)

  
# a = list(range(21))

# shuffle(a)
# print(a)
# mergesort(a, 0, len(a)-1)

# print(a)