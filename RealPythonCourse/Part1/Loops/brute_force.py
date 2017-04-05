tries = 0

while tries < 3:
    password = input("Password:")
    if password != 'Icn@support':
        tries += 1
        print('Incorrect Password')
    else:
        print('Access Granted!')
        break
else:
    print('Too much incorrect attempts. Your account has been locked.')