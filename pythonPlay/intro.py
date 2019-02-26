import re

hello_message = 'Hello World'

print(hello_message)

print (len(hello_message))

print(hello_message[:5])
print(hello_message[6:])

matchObject = re.match( r'(.*)World', hello_message, re.I)
print(matchObject.group())