def time(a):
    res=[int(i) for i in a.split(':')]
    return res[0]*60+res[1]
class Tram:
    def __init__(self,id,station,t,rain_amount):
        self.id=id
        self.station=station
        self.rain_amount=rain_amount
        self.t=t
    def setT(self,x):
        self.t+=x
    def setRain(self,x):
        self.rain_amount+=x
    def __str__(self):
        return self.id+" "+self.station+" "+'{:.2f}'.format(self.rain_amount/self.t*60)
ans=dict()
t=int(input())
idx=1
for i in range(t):
    ma='T%02d'%idx
    ten=input()
    bd=input()
    kt=input()
    thoiGian=time(kt)-time(bd)
    mua=float(input())
    if ten in ans:
        ans[ten].setT(thoiGian)
        ans[ten].setRain(mua)
    else:
        ans[ten]=Tram(ma,ten,thoiGian,mua)
        idx+=1
for i in ans:
    print(ans[i])

"""
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""