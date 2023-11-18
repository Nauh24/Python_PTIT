class HoaDon:
    def __init__(self,id,name,soLuong,donGia,tienChietKhau):
        self.id=id
        self.name=name
        self.soLuong=soLuong
        self.donGia=donGia
        self.tienChietKhau=tienChietKhau
    def tongTien(self):
        return self.donGia*self.soLuong-self.tienChietKhau
    def __str__(self):
        return self.id+' '+self.name+' '+str(self.soLuong)+' '+str(self.donGia)+' '+str(self.tienChietKhau)+' '+str(self.tongTien())

a=[]
for t in range(int(input())):
    id=input()
    name=input()
    soLuong=int(input())
    donGia=int(input())
    ck=int(input())
    hd=HoaDon(id,name,soLuong,donGia,ck)
    a.append(hd)
a.sort(key=lambda x:(-x.tongTien()))
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