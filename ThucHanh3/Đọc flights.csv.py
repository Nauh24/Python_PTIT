import csv
with open('flights.csv','r') as f:
    lines=f.readlines()
dong=len(lines)
cot=len(lines[0].split(','))
print(dong-1,cot,sep=' ')