class Underscore:
    def map(self, iterable, callback):
        for index in range(len(iterable)):
          iterable[index] = callback(iterable[index])
        return iterable

    def find(self, iterable, callback):
        for element in iterable:
          if callback(element) == True:
            return element
        return False

    def filter(self, iterable, callback):
        count = 0
        for element in iterable:
          if callback(element) == False:
            count += 1
        for index in range(len(iterable)-count):
          if callback(iterable[index]) == False:
            iterable.pop(index)
        return iterable

    def reject(self, iterable, callback):
        count = 0
        for element in iterable:
          if callback(element) == True:
            count += 1
        for index in range(len(iterable)-count+1):
          if callback(iterable[index]) == True:
            iterable.pop(index)
        return iterable

_=Underscore()
some_list = [1,2,3,4]
# print(_.map(some_list, lambda x: x*10))
# print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 3))
# print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
# print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
