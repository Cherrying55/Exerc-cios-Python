def main():
    x = input("Please type a sentence: ")
    u = preparestring(x)
    p = palindrome(u)
    print(u)
    if p == True:
        print("Palindrome")
    else:
        print("Not palindrome")

def preparestring (x):
    res_x = ""
    for char in x:
        if char.lower() >= "a":
           res_x = res_x + char
    res_x = res_x.lower()
    return res_x       


    
def palindrome(x):
    counter = False
    for i in range(len(x)):
        if x[i] == x[-i-1]:
            counter = True
        else:
            counter = False
    return counter

main()
