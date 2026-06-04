from datetime import date
import csv
dt = date.today()

filename= "test.csv"
exp=[]
stopped = False

with open(filename, 'w') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp= int(input("What is the expense(type 0 to stop:"))
        if xp==0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
        
file.close()
print("your expenses are,", exp)
print("Total expense:", sum(exp))
print("Maximum expense:", max(exp))