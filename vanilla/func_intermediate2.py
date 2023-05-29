#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = "bryant"
sports_directory['soccer'][0] = "andres"
z[0]['y'] = 30

print(x, students, sports_directory, z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#2
def iterateDictionary(list):
    for i in range (len(list)):
        a = list[i]['first_name']
        b = list[i]['last_name']
        print(f"first_name - {a}, last_name - {b}")
iterateDictionary(students)

#3
def iterateDictionary2(key, list):
    for dictionary in list:
        if key in dictionary:
            print(dictionary[key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4
def printInfo(dict):
    for key, value in dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)