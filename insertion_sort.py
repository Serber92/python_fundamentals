def sort(some_list):
  for index in range(1, len(some_list)):
    if some_list[index] < some_list[index-1]:
      some_list[index], some_list[index-1] = some_list[index-1], some_list[index]
      if some_list[index-1] < some_list[index-2]:
        sort(some_list)
  return some_list

print(sort([10,9,8,7,6,5,4,3,2,1]))
