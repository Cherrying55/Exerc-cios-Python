
def store(n):
    lst = []
    u = int(n)
    while n != "done":
        u = int(n)
        lst.append(u)
        n = input()
    return lst

def average(lst):
    average = sum(lst) / len(lst)
    return average

def above_average(average, lst):
    lst2 = []
    for i in lst:
        if i > average:
            lst2.append(i)
    return lst2

def main():
    n = input()
    k = store(n)
    l = average(k)
    print("The average is'", l)
    print("The grades above the average are", above_average(l, k))


main()    
    
            
