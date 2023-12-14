class NhanVien:
    def __init__(self,ma,ten,luong,soNgayCong,phongBan):
        self.ma=ma
        self.ten=ten
        self.luong=luong
        self.soNgayCong=soNgayCong
        self.phongBan=phongBan
    def heSoNhan(self):
        soNam=int(self.ma[1:3])
        if self.ma[0]=='A':
            if soNam<=3: return 10
            elif soNam<=8: return 12
            elif soNam<=15: return 14
            else: return 20
        elif self.ma[0]=='B':
            if soNam<=3: return 10
            elif soNam<=8: return 11
            elif soNam<=15: return 13
            else: return 16
        elif self.ma[0]=='C':
            if soNam<=3: return 9
            elif soNam<=8: return 10
            elif soNam<=15: return 12
            else: return 14
        else:
            if soNam<=3: return 8
            elif soNam<=8: return 9
            elif soNam<=15: return 11
            else: return 13

    def luongThang(self):
        return self.luong*self.soNgayCong*self.heSoNhan()
    def __str__(self):
        return self.ma+' '+self.ten+' '+self.phongBan+' '+str(self.luongThang()*1000)
       # return str(self.heSoNhan())

a=[]
d={}
for i in range(int(input())):
    s=input().split()
    ma=s[0]
    phong=''
    for i in range(1,len(s)):
        phong+=s[i]+' '
    d[ma]=phong
for i in range(int(input())):
    ma=input()
    ten=input()
    luong=int(input())
    ngay=int(input())
    mapb=ma[3:]
    nv=NhanVien(ma,ten,luong,ngay,d[mapb])
    a.append(nv)
for i in a:
    print(i)
'''
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
'''
