def countdown(num):
  temp = []
  for x in range(num, -1, -1):
    temp.append(x)
  return temp

def printReturn(li):
  print(li[0])
  return li[1]

def firstPlLen(li):
  return li[0] + len(li) 

def greater(li):
  if(len(li) < 2):
    return False
  temp = []
  for elem in li:
    if(elem > li[1]):
      temp.append(elem)
  return temp

def this(size, value):
  temp = []
  for num in range(size):
    temp.append(value)
  return temp

 