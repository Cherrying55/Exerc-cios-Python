def main():
    s = input("sentence: ")
    print("The first word is", firstword(s))
    

def firstword(s):
    s2 = s[0:s.find(" ")]
    return s2

main()
