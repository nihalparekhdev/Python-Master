#dictionary { key : value } : curly brackets indicate a dictionary
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

print('Dictionary:', my_dict)
print('Value for key "a":', my_dict['a'])

#Creating my own dictionary with help of strings

personal_info = [
    {
        'name': 'Nihal',
        'age': 25,
        'city': 'New York'
    },
    {
        'name': 'Parth',
        'age': 30,
        'city': 'Los Angeles'
    }
]

print ('Personal Info:', personal_info [0] ['name'])

# Dictionary Key should be immutable, so we can use 
# strings, numbers, tuples as keys but not lists or other dictionaries as they are mutable.

dictionary = {
	123: [1,2,3],
	True: 'hello',
	#here this is not possible as the strings can be changed do
	#we cannot assign it
	(100): True
}

#Another way to create a dictionary is by using the dict() constructor
user2 = dict(name='Nihal', age=25, city='San Francisco')
print('User2 Dictionary:', user2)

#Dictionary methods :get()
user = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print('User Dictionary:', user.get('sector'))

#Dictionary methods :keys(), values(), items()
print('name' in user.keys())
print('Nihal' in user.values())
print('city' in user.items())

#copying a dictionary
user_copy = user.copy()
print('User Copy:', user_copy)

#pop() method removes the specified item from the dictionary
user2.pop('age')
print('User2 after popping age:', user2)

#popitem() method removes the last inserted item from the dictionary
user2.popitem()
print('User2 after popping last item:', user2)

#update() method updates the dictionary with the specified key-value pairs
user.update({'age': 35, 'city': 'Los Angeles'})
print('User after update:', user)

#if any key is not present in the dictionary, it will be added to the dictionary
user.update({'country': 'USA'})
print('User after adding country:', user)

#Clearing a dictionary
user.clear()
print('User after clearing:', user)

