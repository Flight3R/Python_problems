from numpy import array
from time import time
  
class Element:
  id      = None
  value   = None
  width   = None
  height  = None
  area    = None
  density = None
  
  
  def __init__(self, list):
    self.id     = list[0]
    self.value  = list[1]
    self.width  = min(list[2], list[3])
    self.height = max(list[2], list[3])
    self.area   = self.width * self.height
    self.density= self.value/self.area
    
  def __str__(self):
    id     = self.id
    value  = self.value
    width  = self.width
    height = self.height
    
    line = 'id: {:5}, value: {:5}, width: {:5}, height: {:5}'.format(id, value, width, height)
    return line
    
  def load(fileNumber):
    file = open('packages'+str(fileNumber)+'.txt','r').read().splitlines()
    file = file[2:]
    elementList = []

    for line in file:
      line = [int(line.split(',')[i]) for i in range(4)]
      new  = Element(line)
      elementList.append(new)
    
    return elementList
    
class Backpack:
  matrix = []
  side   = None
  area   = None
  
  def __str__(self):
    for row in self.matrix:
      print(row)
  
  def __init__(self, sideLength):
    
    self.matrix = array([[0] * sideLength] * sideLength)
    self.side   = sideLength
    self.area   = sideLength ** 2
    
  def search(self, ver, hor):
    for k in range(self.side-ver+1):
      for i in range(self.side-hor+1):
        if self.matrix[k][i]==0 and self.matrix[k][i+hor-1]==0 and self.matrix[k+ver-1][i]==0 and self.matrix[k+ver-1][i+hor-1]==0:
          if all(self.matrix[k][i + l] == 0 for l in range(1,hor-1)):
            if all(self.matrix[k + l][i] == 0 for l in range(1, ver-1)):
              return (k, i) ### k - vertical, i - horizontal
            
    return (None, None)  
  
  def putIn(self, Ycoord, Xcoord, height, width):
    element = [[1] * width] * height
    self.matrix[Ycoord:Ycoord + height, Xcoord:Xcoord + width] = element

  def simplify(self, elementList):
    elementList.sort(key = lambda x: x.density, reverse = True)
    
    inserted  = []
    leftSpace = self.area
    
    for element in elementList:
      if element.area <= leftSpace:
        inserted.append(element)
        leftSpace -= element.area
    
    return inserted
  
  def pack(self, elementList):
    valueSum = 0
    for element in elementList:
      height =  element.height
      width  = element.width
       
      (y, x) = self.search(height, width)
      if (y, x) != (None, None):
        self.putIn(y, x, height, width)
        valueSum += element.value
        continue
        
      (y, x) = self.search(width, height)
      if (y, x) != (None, None):
        self.putIn(y, x, width, height)
        valueSum += element.value
        continue
      
      elementList.remove(element)
    
    return valueSum

def main(packageNo):
  backpack = Backpack(packageNo)
  elementList = Element.load(packageNo)
  possible = backpack.simplify(elementList)
  start = time()
  value = backpack.pack(possible)
  
  t = round((time() - start), 3)
  line = 'packageNo: {:5}, time: {:7}, value: {:7}'.format(packageNo, t, value)
  print(line)

main(20)
main(100)
main(500)
main(1000)