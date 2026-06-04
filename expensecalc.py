exp = -1
total = 0
maxexp=0
minexp= 10000000
while exp != 0:
    exp = int(input("What is the expense(typpe 0 to stop)"))
    if exp == 0:
        break
    total = total + exp
    if exp>maxexp :
        maxexp = exp
    elif (exp<minexp):
        minexp= exp
print("Your total expense is: " + str(total))
print("Your maximum expense is: " + str(maxexp))
print("Your minimum expense is: " + str(minexp))