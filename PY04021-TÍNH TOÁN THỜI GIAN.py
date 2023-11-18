class Gamer:
    def __init__(self,id,name,timeIn,timeOut):
        self.id=id
        self.name=name
        self.timeIn=timeIn
        self.timeOut=timeOut
        self.calculate()

    def calculate(self):
        i=int(self.timeIn[0:2])*60+int(self.timeIn[3:])
        o=int(self.timeOut[0:2])*60+int(self.timeOut[3:])
        self.time=o-i
    def printTime(self):
        h=int(self.time//60)
        m=int(self.time%60)
        return '{} gio {} phut'.format(h,m)
    def __str__(self):
        return self.id+' '+self.name+' '+self.printTime()
list=[]

for j in range(int(input())):
    id=input()
    name=input()
    timeIn=input()
    timeOut=input()
    g=Gamer(id,name,timeIn,timeOut)
    list.append(g)
list.sort(key=lambda x:(-x.time))
for i in list:
    print(i)

"""
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""