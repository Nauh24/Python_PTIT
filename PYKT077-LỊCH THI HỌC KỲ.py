from datetime import datetime


class MonThi:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class LichThi:
    def __init__(self,maCaThi,mt:MonThi,ngayThi,gioThi,nhomThi):
        self.maCaThi=maCaThi
        self.mt=mt
        self.ngayThi=ngayThi
        self.gioThi=gioThi
        self.nhomThi=nhomThi
        self.time=datetime.strptime(self.ngayThi+' '+self.gioThi,"%d/%m/%Y %H:%M")

    def __str__(self):
        return self.maCaThi+' '+self.mt.id+' '+self.mt.name+' '+self.ngayThi+' '+self.gioThi+' '+self.nhomThi

n,m=map(int,input().split())
d={}
for i in range(n):
    id=input()
    name=input()
    mt=MonThi(id,name)
    d[id]=mt
a=[]
for i in range(m):
    maCaThi="T%03d"%(i+1)
    s=input().split()
    maMon=s[0]
    ngay=s[1]
    gio=s[2]
    nhom=s[3]
    lt=LichThi(maCaThi,d[maMon],ngay,gio,nhom)
    a.append(lt)
a.sort(key=lambda x:(x.time,x.mt.id))
for i in a:
    print(i)

'''
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
'''