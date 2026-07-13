#Reverse a string and a list in Python
basket = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
basket.reverse()
print('Reversed basket:', basket)
print('Basket after slicing reverse:', basket[::-1])

#range
print('Range of 100:', list(range(0,101)))

#Join
list = ''
print('Join of list:', list)
new_list = list.join(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print('New list after join:', new_list)

#List unpacking
#Here others will be a list of all the remaining elements after a,b,c and d
a,b,c, *others, d = [1,2,3,4,5,6,7,8]
print (a)
print (b)
print (c)
print (others)
print (d) 