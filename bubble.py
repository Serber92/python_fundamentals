def bubble(some_list, boo=False):
  while(not boo):
    boo = True
    for index in range(len(some_list)-1):
      if some_list[index]>some_list[index+1]:
        some_list[index], some_list[index+1] = some_list[index+1], some_list[index]
        boo = False
      elif index == len(some_list)-1 and not boo:
        boo = not boo
  return some_list

print(bubble([10,9,8,7]))



    
