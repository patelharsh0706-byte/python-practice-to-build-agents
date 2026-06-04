name=input("what is your name?")
age=int(input("what is your age?"))
for50= 50-age
if age>=50:
    over50= age -50
    print("Hello " +name.title() + " You were 50 " +str(over50) + " year ago")
else:
    print("Hello " +name.title() + " You've still got " + str(for50) + "Years. Enjoy!!" ) 