class Student:

    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
        self.avg=total/12
    def rank(self):
        if self.avg>=9:
            return 'XUAT SAC'
        if self.avg>=8:
            return 'GIOI'
        if self.avg>=7:
            return 'KHA'
        if self.avg>=5:
            return 'TB'
        return 'YEU'
    def __str__(self):
        return self.id+' '+self.name+' '+'{:.1f}'.format(self.avg)+' '+self.rank()

t=int(input())
list=[]
for i in range(t):
    id='HS%02d'%(i+1)
    ten=input()
    a=[float[j] for j in input().split()]
    total=sum(a)+a[0]+a[1]
    list.append(Student(id,ten,total))
    for i in list:
        print(i)
"""
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""