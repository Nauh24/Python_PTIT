class SinhVien:
    def __init__(self,id,name,lop):
        self.id=id
        self.name=name
        self.lop=lop
        self.dcc=10
    def setDcc(self,s):
        cnt=10
        for i in s:
            if i=='m':
                cnt-=1
            elif i=='v': cnt-=2
        if cnt<0: cnt=0
        self.dcc=cnt
    def printf(self):
        print(self.id+" "+self.name+" "+self.lop+" "+str(self.dcc),end=' ')
        if self.dcc==0:
            print('KDDK')
        print()


n=int(input())
a=[]
d={}
for _ in range(n):
    id=input()
    name=input()
    lop=input()
    sv=SinhVien(id,name,lop)
    d[sv.id]=sv
    a.append(sv)
for _ in range(n):
    id,status=input().split()
    d[id].setDcc(status)
for i in a:
    i.printf()

'''
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
'''