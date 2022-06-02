def change_lst(lst):
    for i in range(len(lst)):
        lst[i] = (lst[i])**2
    return lst

def create_new_lst(lst):
    lst2 = []
    for i in lst:
        lst2.append(i**2)
    return lst2

def main1():
    lst = [1,2,3]
    lst2 = create_new_lst(lst)
    print(lst, lst2)

def main2():
    lsta = [1,2,3]
    change_lst(lsta)
    print(lsta)
    

main1()
main2()
    
        
