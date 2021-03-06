def naive(list,P,V):
  counter=0
  m=len(P)
  o=len(V)
  n=len(list[0])

  for k in range(n-o+1):
    for i in range(n-m+1):
      if list[k][i:i+m]==P:
        if all(list[k+l][i]==V[l] for l in range(1,o)):
          counter+=1

  print(counter)

def prepareHash(list,P,V,d,q):
  n=len(list[0])
  m=len(P)
  o=len(V)
  h=pow(d,(m-1))%q 
   
  SP=0
  for i in range(m):
    SP=(d*SP + P[i]) % q
    
  STlist=[]
  
  for k in range(n-o+1):
    STrow=[] 
    ST=0
    for i in range(m):
      ST = (d*ST + list[k][i]) % q
    STrow.append(ST)
    for s in range(n-m):
      ST=(d*(ST-list[k][s]*h)+list[k][s+m])%q
      STrow.append(ST)  
   
    STlist.append(STrow)

  return SP,STlist

def rabin(list,P,V,SP,ST):
  n=len(list[0])
  m=len(P)
  o=len(V)
  
  counter=0
  
  for k in range(n-o+1):
    for s in range(n-m+1):
      if SP==ST[k][s]:
        if P==list[k][s:s+m]:
          if all(list[k+l][s]==V[l] for l in range(1,o)):
            counter+=1
  print(counter)

#--------- MAIN:
from time import *
nTimes=[]
rTimes=[]
files=[1000,2000,3000,4000,5000,8000]

for fi in files:
  # wczywtywanie pliku do tablicy i zmiana na liczby
  f=open(str(fi)+'_pattern.txt','r').read()
  lines=f.splitlines()
  list=[]
  for li in lines:
    x=[ord(i) for i in li]
    list.append(x)
  
  """  A B C
       B
       C
  """  
  P=[ord(x) for x in 'ABC'] # poziomo
  V=[ord(x) for x in 'ABC'] # pionowo
  SP,ST=prepareHash(list,P,V,256,101)
  
  nTimes.append('----'+str(fi)+'----')
  rTimes.append('----'+str(fi)+'----')
  for n in range(10): 
    start=time()
    naive(list,P,V)
    nTimes.append(time()-start)

    start=time()
    rabin(list,P,V,SP,ST)
    rTimes.append(time()-start) 

print('naive') 
for i in nTimes:
  print(i)
  
print('rabin')
for i in rTimes:
  print(i)
  