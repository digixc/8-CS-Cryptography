import hashlib
import binascii
hashedPassword='2b058ab133ff919bb39ebf7ceb1c13e5'

with open('passwords.txt','r') as textFile:
        passwordList = textFile.read()

passwords = passwordList.split('\n')

hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)

for password in passwords:
        hashed = hashlib.pbkdf2_hmac('sha256',bytes(password,'utf-8'),b'salt',10000)
        #hashed = hashlib.md5(password.encode('utf-8')).hexdigest()
        if hashed == hashedPassword:
                print('Password is '+password)
                break
        

        
