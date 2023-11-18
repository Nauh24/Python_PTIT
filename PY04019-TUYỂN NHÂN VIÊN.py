class NhanVien:
    def __init__(self,id,name,lt,th):
        self.name=name
        self.id=id
        self.lt=lt
        self.th=th

    def check(self):
        if self.lt>10:
            self.lt/=10
        if self.th>10:
            self.th/=10
    def diemTB(self):
        self.check()
        return (self.lt+self.th)/2
    def status(self):
        if self.diemTB()<5: return "TRUOT"
        if self.diemTB()<8: return "CAN NHAC"
        if self.diemTB()<=9.5: return "DAT"
        return "XUAT SAC"
    def __str__(self):
        return self.id+' '+self.name+' '+'{:.2f}'.format(self.diemTB())+' '+self.status()

list=[]
i=0
for j in range(int(input())):
    id="TS0%1d"%(i+1)
    i+=1
    s=input()
    lt=float(input())
    th=float(input())
    nv=NhanVien(id,s,lt,th)
    list.append(nv)
list.sort(key=lambda x:(-x.diemTB()))
for i in list:
    print(i)

"""
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
"""