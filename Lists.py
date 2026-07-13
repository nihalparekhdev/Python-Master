#Lists are used to store multiple items in a single variable.
amazon_cart = ["laptop", "headphones", "mouse", "keyboard"]
print(amazon_cart[0]) 

#List slicing
amazon_cart = ["laptop", "headphones", "mouse", "keyboard"]
print(amazon_cart[0:3]) # ['laptop', 'headphones', 'mouse']
print(amazon_cart[0:4:2]) # ['laptop', 'mouse']

#Lists are mutable, meaning you can change their content without changing their identity.
amazon_cart [0] = 'Television'
print('Updated changed amazon_cart:', amazon_cart) 

#Matrix : 2D List which contains multiple lists inside a single list which can be also called arrays of array

matrix = [[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['nihal', 'parth', 'abhi']
]]

#here the [0] is main list, [3] is the subarray and [1] is the index of the subarray
print('Matrix will be :', matrix [0] [3] [1])


#List/Array Methods
#append() : Adds an element at the end of the list
basket = [1,2,3,4,5]
basket.append('nihal')
new_basket = basket
print('New appended basket:', new_basket)

#insert() : Adds an element at the specified position
basket.insert(4, 'parth')
updated_basket = basket
print('Updated basket:', updated_basket)

#extend() : Add the elements of a list (or any iterable), to the end of the current list
basket.extend(['abhi', 'vaidehi'])
extended_basket = basket
print('Extended basket:', extended_basket)

#remove() : Removes the first item with the specified value
basket.remove('abhi')
removed_basket = basket
print('Removed basket:', removed_basket)

#pop() : Removes the element at the specified position
basket.pop(0)
popped_basket = basket
print('Popped basket:', popped_basket)

#clear() : Removes all the elements from the list
basket.clear()
cleared_basket = basket
print('Cleared basket:', cleared_basket)

#index() : Returns the index of the first element with the specified value
basket = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
index_of_cherry = basket.index('cherry')
print('Index of cherry:', index_of_cherry)

#count() : Returns the number of elements with the specified value
basket = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'banana']
count_of_banana = basket.count('banana')
print('Count of banana:', count_of_banana)




