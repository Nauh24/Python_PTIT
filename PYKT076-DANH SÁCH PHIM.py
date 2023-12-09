from datetime import datetime


class TheLoai:
    def __init__(self,id,theloai):
        self.id=id
        self.theloai=theloai
class Phim:
    def __init__(self,tl:TheLoai,id,ngay,tenFilm,soTap):
        self.tl=tl
        self.id=id
        self.ngay=ngay
        self.tenFilm=tenFilm
        self.soTap=soTap
        self.time=datetime.strptime(self.ngay,"%d/%m/%Y")
    def __str__(self):
        return self.id+' '+self.tl.theloai+' '+self.ngay+' '+self.tenFilm+' '+str(self.soTap)
n,m=map(int,input().split())
mtl={}
for i in range(n):
    id="TL%03d"%(i+1)
    ten=input()
    tl=TheLoai(id,ten)
    mtl[id]=tl
a=[]
for j in range(m):
    id="P%03d"%(j+1)
    matl=input()
    ngay=input()
    ten=input()
    soTap=int(input())
    film=Phim(mtl[matl],id,ngay,ten,soTap)
    a.append(film)
a.sort(key=lambda x: (x.time,x.tenFilm,-x.soTap))
for i in a:
    print(i)
'''
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
'''