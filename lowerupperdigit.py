x = input("Please type a character: ")

if x < "a" and x < "0":
    print(x, "is a non-alphanumeric character.")
elif x <"a" and x >= "0":
    print(x, "is a digit.")
elif x >= "a" and x.upper() == x:
    print(x, "is a upper case letter.")
else:
    print(x, "is a lower case letter.")
    
