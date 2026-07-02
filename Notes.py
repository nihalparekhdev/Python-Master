#string indices topic   
# [start:end:stepover]
selfish = "dev"
print(selfish[0:8:2]) # 0246
print(selfish[1:]) # 1234567
print(selfish[:5]) # 01234
print(selfish[::1]) # 01234567
print(selfish[-1]) # 7 in negative integers it counts from the end
print(selfish[::-1]) # this starts from the end and goes to the start 


#Immutabillity : the parts of the strubgs cannot be changes  but the whole string can be changed 


#Build in string methods
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote)

#Booleans : It can either be true or false
print (bool(0))
print (bool(1))
is_cool = True
is_cool = False

#Comments in Python 