from datetime import datetime


class MonThi:
    def __init__(self,ma,ten,hinhThuc):
        self.ma=ma
        self.ten=ten
        self.hinhThuc=hinhThuc
    
class CaThi:
    def __init__(self,ma,ngayThi,gioThi,phongThi):
        self.ma=ma
        self.ngayThi=ngayThi
        self.gioThi=gioThi
        self.phongThi=phongThi
        self.time=datetime.strptime(ngayThi+' '+gioThi,'%d/%m/%Y %H:%M')

class LichThi:
    def __init__(self,mt:MonThi,ct:CaThi,nhomLop,soLuong):
        self.mt=mt
        self.ct=ct
        self.nhomLop=nhomLop
        self.soLuong=soLuong
    def __str__(self):
        return self.ct.ngayThi+' '+self.ct.gioThi+' '+self.ct.phongThi+' '+self.mt.ten+' '+self.nhomLop+' '+self.soLuong
    
fmt=open('MONTHI.in','r')
fct=open('CATHI.in','r')
flt=open('LICHTHI.in','r')
mmt,mct={},{}
n=int(fmt.readline().strip())
for i in range(n):
    mt=MonThi(fmt.readline().strip(),fmt.readline().strip(),fmt.readline().strip())
    mmt[mt.ma]=mt
m=int(fct.readline().strip())
for i in range(m):
    ma="C%03d"%(i+1)
    ngayThi=fct.readline().strip()
    gioThi=fct.readline().strip()
    phongThi=fct.readline().strip()
    ct=CaThi(ma,ngayThi,gioThi,phongThi)
    mct[ma]=ct
k=int(flt.readline().strip())
a=[]
for i in range(k):
    s=flt.readline().strip().split()
    maCt=s[0]
    maMon=s[1]
    nhom=s[2]
    sl=s[3]
    lt=LichThi(mmt[maMon],mct[maCt],nhom,sl)
    a.append(lt)
a=sorted(a,key=lambda x: (x.ct.time,x.ct.ma))
for i in a:
    print(i)