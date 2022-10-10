char=input('enter a character=')

asc=ord(char)
print("ASCII equivalent is given as =",asc )


if ( 'A'<= char<= 'Z'):
    print("the given character is in Upper case")
elif ( 'a'<= char <='z'):
    print(" the given character is in lower case")
else:
    print("error")
