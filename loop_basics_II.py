def positive(lis):
  for index in range(len(lis)):
    if(lis[index]>0):
      lis[index] = "big"
  return lis

def countPos(lis):
  count = 0
  for elem in lis:
    if(elem > 0):
      count += 1
  lis.pop()
  lis.append(count)
  return lis

def sum1(lis):
  s = 0
  for elem in lis:
    s += elem
  return s

def av(lis):
  return sum(lis)/len(lis)

def length(lis):
  return len(lis)

def minimum(lis):
  return min(lis)

def ult(lis):
  dic = {
    "total":sum(lis),
    "average":av(lis),
    "min":min(lis),
    "max":max(lis),
    "length":len(lis)
  }
  return dic

def rev(lis):
  length = len(lis)
  for index in range(0,round(length/2)):
    lis[index], lis[length-1-index] = lis[length-1-index], lis[index]
  return lis


    
