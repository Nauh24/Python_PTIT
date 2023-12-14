from math import ceil


class SinhVien:
    def __init__(self,id,name,d1,d2,d3):
        self.name=name
        self.id=id
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.avg=(self.d1*3+self.d2*3+self.d3*2)/8
    def chuanHoaName(self):
        s=self.name.split()
        res=' '.join(s)
        return res.title()
    def __str__(self):
        return self.id+' '+self.chuanHoaName()+' '+'{:.2f}'.format(ceil(self.avg*100)/100)
a=[]
for t in range(int(input())):
    id="SV%02d"%(t+1)
    name=input().strip()
    d1=int(input())
    d2=int(input())
    d3=int(input())
    sv=SinhVien(id,name,d1,d2,d3)
    a.append(sv)
a.sort(key=lambda x:(-x.avg,x.id))
cnt=0
res=0
diem=0
for i in a:
    if diem!=i.avg:
        res+=cnt
        cnt=0
        res+=1
    else :
        cnt+=1
    print(i,res,sep=' ')
    diem=i.avg
'''
3
Pham    THI  HAO
6
7
6
 ha Thi kieu     anh
7
6
7
Pham    VAN hUan
6
7
6
'''