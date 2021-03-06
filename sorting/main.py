from random import *
from time import *
from insertion import *
from merge import *

n = 20 #sortowan
lista = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
TInsMax=[]
TInsMin=[]
TInsSr=[]
TInsCalk=[0]*len(lista)

TMrgMax=[]
TMrgMin=[]
TMrgSr=[]
TMrgCalk=[0]*len(lista)


print('elementy:')
for i in range(len(lista)):
  insmax=0
  insmin=1000
  mrgmax=0
  mrgmin=1000
  #przygotowywanie tablic
  k=lista[i]
  print(k)
  for j in range(n):
    tab = list(range(k))
    shuffle(tab)
    tab2 = tab[:]
  #ins sort
    start = time()
    insertionsort(tab,len(tab))
    t=time() - start
    if t > insmax:
      insmax=t
    if t < insmin:
      insmin=t
    TInsCalk[i]+=t
  #mrg sort
    start = time()
    mergesort(tab2,0,len(tab)-1)
    t=time() - start
    if t > mrgmax:
      mrgmax=t
    if t < mrgmin:
      mrgmin=t
    TInsCalk[i]+=t
    TMrgCalk[i]+=t
    
  TInsSr.append(TInsCalk[i]/n)
  TInsMax.append(insmax)
  TInsMin.append(insmin)
  
  TMrgSr.append(TMrgCalk[i]/n)
  TMrgMax.append(mrgmax)
  TMrgMin.append(mrgmin)
  
  ins_sum = 0
  mrg_sum = 0
 
  # print('{0}\t {1}\t\t {2}'.format('operacja', 'ins. sort', 'mergesort'))
  # print('{0}\t {1}\t\t {2}'.format('T całkowity', ins_sum, mrg_sum))
  # print('{0}\t {1}\t\t {2}'.format('sredni T ', ins_sum/n, mrg_sum/n))
  # print('{0}\t {1}\t\t {2}'.format('T maksymalny', max(ins_time), max(mrg_time)))
  # print('{0}\t {1}\t\t {2}'.format('T minimalny', min(ins_time), min(mrg_time)))
  
print('Ins Tcałk')
for i in TInsCalk:
  print (i)
print('Ins Tśr')
for i in TInsSr:
  print (i)
print('Ins Tmax')
for i in TInsMax:
  print (i)
print('Ins Tmin')
for i in TInsMin:
  print (i)
print('Mrg Tcałk')
for i in TMrgCalk:
  print (i)
print('Mrg Tśr')
for i in TMrgSr:
  print (i)
print('Mrg Tmax')
for i in TMrgMax:
  print (i)
print('Mrg Tmin')
for i in TMrgMin:
  print (i)
