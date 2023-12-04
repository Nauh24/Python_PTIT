from datetime import datetime


class KhachHang:
    def __init__(self,id,name,soPhong,soNgay,tienPhatSinh):
        self.id=id
        self.name=name
        self.soPhong=soPhong
        self.soNgay=soNgay
        self.tienPhatSinh=tienPhatSinh
    def donGia(self):
        if self.soPhong[0]=='1': return 25
        elif self.soPhong[0]=='2': return 34
        elif self.soPhong[0]=='3': return 50
        else : return 80
    def thanhTien(self):
        return self.soNgay*self.donGia()+self.tienPhatSinh
    def printf(self):
        print(self.id+' '+self.name+' '+self.soPhong+' '+str(self.soNgay)+' '+str(self.thanhTien()))

n=int(input())
a=[]
for i in range(n):
    id='KH%02d'%(i+1)
   
    name=input()
    soPhong=input()
    date_format="%d/%m/%Y"
    ngayDen=datetime.strptime(input().strip(),date_format)
    ngayDi=datetime.strptime(input().strip(),date_format)
    soNgay=(ngayDi-ngayDen).days+1
    tinePhatSinh=int(input())
    kh=KhachHang(id,name,soPhong,soNgay,tinePhatSinh)
    a.append(kh)
a.sort(key=lambda x: -x.thanhTien())
for i in a:
    i.printf()
'''
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
'''