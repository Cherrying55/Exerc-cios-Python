x = input()

print("Your first name is", x[0:x.find(" ")], "and your second name is", x[x.find(" ") + 1: len(x)], "and your initials are", x[0] + x[x.find(" ") + 1])


      
