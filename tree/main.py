class Wezel:
  def __init__(self, wartosc=None, lewy=None, prawy=None):
    self.wartosc=wartosc
    self.lewy=lewy
    self.prawy=prawy

  def __str__(self):
    return str(self.wartosc)
  
""" funkcje wyswietlajace """
def wyswietl(lista):
  for i in lista:
    wyswietl_prog(i,0)
    print()
    
def wyswietl_prog(wezel,t):
  print(t*'-'+str(wezel),end='')
  if wezel.lewy:
    wyswietl_prog(wezel.lewy,t+1)
  if wezel.prawy:
    print()
    print((t+1)*'   '+t*' ',end='')
    wyswietl_prog(wezel.prawy,t+1)              

""" funkcje szukajace """ 
def szukaj(lista, x):
  cal=x//1
  l=len(lista)
  i=0
  if cal<lista[0].wartosc or cal>lista[-1].wartosc:
    return False
  while i<l and lista[i].wartosc<cal:
    i+=1
  tmp=lista[i]
  while True:
    if x==tmp.wartosc:
      return True
    elif x<tmp.wartosc:
      if tmp.lewy:
        tmp=tmp.lewy 
      else:
        return False      
    elif x>tmp.wartosc:
      if tmp.prawy:
        tmp=tmp.prawy 
      else:
        return False
    else:
      return False

"""wstawianie wezla"""
def wstaw(lista,x):
  cal=x//1
  dlugosc=len(lista)
  i=0
  while i<dlugosc and lista[i].wartosc<cal:
    i+=1
  if i==dlugosc or cal+0.5!=lista[i].wartosc:
    rootx=Wezel(cal+0.5)
    lista.insert(i,rootx)
    
  tmp=lista[i]
  while True:
    if tmp.wartosc==x:
      return False
    elif x<tmp.wartosc:
      if tmp.lewy:
        tmp=tmp.lewy
      else:
        tmp.lewy=Wezel(x)
        return True
    elif x>tmp.wartosc:
      if tmp.prawy:
        tmp=tmp.prawy
      else:
        tmp.prawy=Wezel(x)
        return True
    
"""minimum i maksimum"""
def minimum(wezel):
  w=wezel
  while w.lewy:
    w=w.lewy
  return w
    
def maximum(wezel):
  w=wezel
  while w.prawy:
    w=w.prawy
  return w
    
""" budowanie drzewa """
def buduj():
  root1=Wezel(1.5)
  root2=Wezel(3.5)
  root3=Wezel(4.5)
  root4=Wezel(7.5)
  root5=Wezel(9.5)

  lista=[root1,root2,root3,root4,root5]

  lista[0].lewy=Wezel(1.3)
  lista[0].prawy=Wezel(1.6)

  lista[1].lewy=Wezel(3.7)

  lista[2].lewy=Wezel(4.0)
  lista[2].prawy=Wezel(4.99)

  lista[3].lewy=Wezel(7.3)
  lista[3].prawy=Wezel(7.8)
  lista[3].prawy.lewy=Wezel(7.7)
  lista[3].prawy.prawy=Wezel(7.9)
  lista[3].prawy.lewy.lewy=Wezel(7.6)
  lista[4].lewy=Wezel(9.3)
  
  return lista
  
# lista=buduj()
# wstaw(lista,3.5)
# wstaw(lista,2.9)
# wstaw(lista,10)
# wstaw(lista,7.77) 
# wstaw(lista,11.89) 
# wstaw(lista,11.12) 
# wstaw(lista,11.92) 
# wstaw(lista,11.98) 
    
# print('minimum:',minimum(lista[0]))
# print('maximum:',maximum(lista[-1]))

# wyswietl(lista)

# print('z') if szukaj(lista,7.77) else print('n')

from random import *
from time import *

# el=[250,500,1000,5000,10000] 
el=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] 

Lczasy=[] #lista na podlisty zawierajace czasy: wstaw, wysw, szukaj 100el, min, max dla n elementow

for numer in el:
  los=[0]*numer
  zakres=numer/5
  for i in range(numer):
    los[i]=round(uniform(1,zakres),2)
  
  czasy=[] #lista na czasy n elementow
  lista=buduj()
  
  start=time()
  for i in los:
    wstaw(lista,i)
  czasy.append(time()-start)

  start=time()
  wyswietl(lista)
  czasy.append(time()-start)
  
  doszukania=[]
  for i in range(1000):
    doszukania.append(round(uniform(1,zakres),2))
    
  start=time()
  for i in doszukania:
    print('z') if szukaj(lista,i) else print('n')
  czasy.append((time()-start))

  start=time()
  print('min:',minimum(lista[0]))
  czasy.append(time()-start)
  
  start=time()
  print('max:',maximum(lista[-1]))
  czasy.append(time()-start)
  
  Lczasy.append(czasy)
  
# print('wstaw\nwyswietlanie\nszukaj\nminimum\nmaximum') 
# for lista,e in zip(Lczasy,el):
  # print('elementy:',e)
  # for j in lista:
    # print(j)
for i in el:
  print(i)

for i in range(5):
  print('----------')
  for l in Lczasy:
    print(l[i])
 
