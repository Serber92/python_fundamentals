def sort(some_list):
  for index in range(len(some_list)):
    some_list[index], some_list[some_list.index(min(some_list))] = min(some_list), some_list[index]
    some_list[index] *=100
  some_list=[round(x/100) for x in some_list]
  return some_list

print(sort([10,9,8,7,6,5,4,3,2,1]))
