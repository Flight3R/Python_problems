from math import sqrt,inf
from random import *

"""FILE LOAD"""
file=open('TSP.txt','r')
map=[]
for line in file:
  city=[float(line.split()[i]) for i in range(3)]
  map.append(city)
  
"""COSTS MATRIX"""
matrix=[]
for vertical in map:
  line=[]
  for horizontal in map:
    dist=sqrt((vertical[1]-horizontal[1])**2+(vertical[2]-horizontal[2])**2)
    line.append(dist)
  matrix.append(line)

"""PRINT"""
# for y in range(10):
  # for x in range(10):
    # print('{:20}'.format(matrix[y][x]),end='')
  # print()
  
order=list(range(1,101))
shuffle(order)

prev=order[-1]
for i in order:
  dist+=matrix[i-1][prev-1]
  prev=i

order[0],order[-1]=order[-1],order[0] 
print(order,dist)
print() 

bestPath=None
bestCost=inf
for k in range(100):
  v=k
  path=[v]
  cost=0
  for j in range(99):
  
    minCost=inf
    for i in matrix[v]:
      if i<minCost and i!=0 and not matrix[v].index(i) in path:
        minCost=i 
    
    next=matrix[v].index(minCost)
    cost+=minCost
    path.append(next)
    v=next
    
  cost+=matrix[path[-1]][k]
    
  if cost<bestCost:
    bestCost=cost
    bestPath=path

for i in range(len(bestPath)):
  bestPath[i]+=1
  
print(bestPath,bestCost,len(bestPath))

