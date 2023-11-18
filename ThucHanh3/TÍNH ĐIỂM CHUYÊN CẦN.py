class SinhVien:
    def __init__(self,id,name,lop):
        self.id=id
        self.name=name
        self.lop=lop
        self.cc=10
    def cal(self,s):
        for i in s:
            if i=='m': self.cc-=1
            elif i=='v': self.cc-=2
        if self.cc<=0:
            self.cc=0
    def out(self):
        print(self.id+' '+self.name+' '+self.lop+' '+str(self.cc),end='')
        if self.cc==0:
            print(' KDDK',end='')
        print()
a=[]
m={}
t=int(input())
for i in range(t):
    id=input()
    name=input()
    lop=input()

    sv= SinhVien(id,name,lop)
    m[id]=sv
    a.append(sv)
for i in range(t):
    id,s=input().split()
    m[id].cal(s)
for i in a:
    i.out()

"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""