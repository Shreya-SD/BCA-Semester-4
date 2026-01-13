str="Welcome to Python"
print("the string is:",str)
print("the first element is:",str[0])
print("elements from 4 to 8 are:",str[5:9])
print("elements from 4 are:",str[5:])
print("twice the string is:",str*2)
print("length of string is:",len(str))
print("string in lowercase:",str.lower())
print("string in uppercase:",str.upper())
print("string in swapping case:",str.swapcase())
print("capitalize:",str.capitalize())
print("title:",str.title())

str="Hello"
print("string is upper:",str.isupper())
print("string is lower:",str.islower())

str="123"
print("string is digit:",str.isdigit())

str="Hello"
print("string has '1' in it:",'1' in str)
print("string doesn't have 'a':",'a' not in str)
