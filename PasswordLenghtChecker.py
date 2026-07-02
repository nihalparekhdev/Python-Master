username = (input("Enter your username: "))
password = (input("Enter your password: "))
password_length = len(password)
encrypted_password = '*' * password_length

print (f'Your username is: {username} and your password is: {encrypted_password} and the length of your password is: {password_length}')
