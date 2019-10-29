# 1.

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]["last_name"] = "Bryat"
sports_directory['soccer'][0] = "Andres"
z[0]["y"] = 30

# 2.

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(lis):
    boo = True
    for elem in lis:
        for key, val in elem.items():
            if (boo):
                print(key, "-", val + ",", end=" ")
                boo = not boo
            elif (not boo):
                print(key, "-", val)
                boo = not boo

def iterateDictionary2(key_name, some_list):
    for di in some_list:
            print(di[key_name])



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print("\n", len(some_dict[key]), key.upper())
        for elem in some_dict[key]:
            print(elem)


