import Security

status, kc = Security.SecKeychainOpen('~/Library/Keychains/login.keychain', None)
if status == 0:
    print('success')



