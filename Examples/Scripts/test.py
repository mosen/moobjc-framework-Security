import Security

status, kc = Security.SecKeychainOpen('~/Library/Keychains/login.keychain', None)
if status != 0:
    raise Exception('Couldnt open keychain')

status, settings = Security.SecKeychainCopySettings(kc, None)
if status != 0:
    raise Exception('Couldnt get settings')

print(settings)

status, searchList = Security.SecKeychainCopyDomainSearchList(Security.kSecPreferencesDomainUser, None)
if status != 0:
    raise Exception('Couldnt get user domain search list')

print(searchList)




