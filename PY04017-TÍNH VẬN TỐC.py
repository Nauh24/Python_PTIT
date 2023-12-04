class Cuaro:
    def __init__(self,name,add,startTime):
        self.name=name
        self.add=add
        self.startTime=startTime
    def id(self):
        a=self.add.split()
        s=''
        for i in a:
            s+=i[0]
        b=self.name.split()
        for i in b:
            s+=i[0]
        return s
    def vanToc(self):
        st=self.startTime.split(':')
        tmp=int(st[0])+int(st[1])/60-6
        return 120/tmp
    def __str__(self):
        return self.id()+' '+self.name+' '+self.add+' '+str(round(self.vanToc()))+' '+'Km/h'

n=int(input())
a=[]
for i in range(n):
    name=input()
    add=input()
    st=input()
    cr=Cuaro(name,add,st)
    a.append(cr)
a.sort(key=lambda x: -x.vanToc())
for i in a:
    print(i)
'''
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
'''