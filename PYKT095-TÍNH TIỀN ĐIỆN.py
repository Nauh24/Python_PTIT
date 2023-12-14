class KhachHang:
    def __init__(self,id,name,loai,csDau,csCuoi):
        self.id=id
        self.name=name.strip()
        self.loai=loai
        self.csDau=csDau
        self.csCuoi=csCuoi
    def chuanHoaName(self):
        s=self.name.lower().split()
        res=' '.join(s)

        return res.title()
    def dinhMuc(self):
        if self.loai=='A': return 100
        elif self.loai=='B': return 500
        else: return 200
    def soDien(self):
        return self.csCuoi-self.csDau
    def tienTrongDinhMuc(self):
        if self.soDien()<self.dinhMuc(): return self.soDien()*450
        else : return self.dinhMuc()*450
    def tienVuotDinhMuc(self):
        if self.soDien()>self.dinhMuc(): return (self.soDien()-self.dinhMuc())*1000
        else: return 0
    def thue(self):
        return self.tienVuotDinhMuc()//20
    def thanhTien(self):
        return self.tienTrongDinhMuc()+self.tienVuotDinhMuc()+self.thue()
    def __str__(self):
        return self.id+' '+self.chuanHoaName()+' '+str(self.tienTrongDinhMuc())+' '+str(self.tienVuotDinhMuc())+' '+str(self.thue())+' '+str(self.thanhTien())

a=[]
for i in range(int(input())):
    id="KH%02d"%(i+1)
    name=input()
    s=input().split()
    loai=s[0]
    dau=int(s[1])
    cuoi=int(s[2])
    kh=KhachHang(id,name,loai,dau,cuoi)
    a.append(kh)
a.sort(key=lambda  x: (-x.thanhTien()))
for i in a:
    print(i)

'''
2
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 160
'''