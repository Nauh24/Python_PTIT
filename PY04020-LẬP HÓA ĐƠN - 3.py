class HoaDon:
    def __init__(self,id,name,slMua,donGia,chietKhau):
        self.id=id
        self.name=name
        self.slMua=slMua
        self.donGia=donGia
        self.chietKhau=chietKhau
    def tongTien(self):
        return self.donGia*self.slMua-self.chietKhau
    def __str__(self):
        return self.id+' '+self.name+' '+str(self.slMua)+' '+str(self.donGia)+' '+str(self.chietKhau)+' '+str(self.tongTien())
    
n=int(input())
a=[]
for i in range(n):
    id=input()
    name=input()
    sl=int(input())
    dg=int(input())
    ck=int(input())
    hd=HoaDon(id,name,sl,dg,ck)
    a.append(hd)
a.sort(key=lambda x: -x.tongTien())
for i in a:
    print(i)

'''
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
'''