import array
import Security

status, kc = Security.SecKeychainOpen('~/Library/Keychains/login.keychain', None)
if status:
    raise Exception('Couldnt open keychain')

status, settings = Security.SecKeychainCopySettings(kc, None)
if status:
    raise Exception('Couldnt get settings')

print(settings)

status, searchList = Security.SecKeychainCopyDomainSearchList(Security.kSecPreferencesDomainUser, None)
if status:
    raise Exception('Couldnt get user domain search list')

print(searchList)

# for sl in searchList:
#     path_len = 1024
#     #path_buf = array.array('c','\0'*path_len)
#     path_buf = ""
#     status, path_len, path_buf = Security.SecKeychainGetPath(sl, path_len, path_buf)
#     print(path_buf[:path_len].tostring())


# status, access = Security.SecKeychainCopyAccess(kc, None)
# if status != 0:
#     errMsg = Security.SecCopyErrorMessageString(status, None)
#     raise Exception('Couldnt copy access: {}'.format(errMsg))
#
# print(access)

# status, kcstatus = Security.SecKeychainGetStatus(kc, None)
# if status:
#     raise Exception('Cant get status')
#
# print(kcstatus)


status, result = Security.SecItemCopyMatching({
    Security.kSecClass: Security.kSecClassCertificate,
    Security.kSecMatchLimit: Security.kSecMatchLimitAll
}, None)

print(result)


