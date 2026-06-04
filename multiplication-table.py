num= int(input("Enter a number to see its multiplication table: "))
mx= [num * x for x in range(1,11)]

mx2= [str(x)+ 'x' + str(num) + '=' + str(num * x) for x in range(1,11)]

mx3= [f"{x} x {num} = {num * x}" for x in range(1,11)]

print(mx3)