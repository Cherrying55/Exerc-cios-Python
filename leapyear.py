def main():
    b = int(input("year; "))
    if leap(b) == True:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")

def leap (y):
    b = False
    if y % 4 !=0 or y % 4 == 0 and y % 400 !=0:
        b = False
    else:
        b = True
    return b

main()
