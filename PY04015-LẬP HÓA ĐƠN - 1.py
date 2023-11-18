class HoaDon:
    def __init__(self,id,name,hieuChiSo):
        self.id=id
        self.name=name
        self.hieuChiSo=hieuChiSo
        self.total()

    def total(self):
        if self.hieuChiSo<=50: return self.hieuChiSo*100+self.hieuChiSo*100*0.02
        elif self.hieuChiSo<=100: return (50*100+(self.hieuChiSo-50)*150)*1.03
        else:return (50*100+50*150+(self.hieuChiSo-100)*200)*1.05
    def __str__(self):
        return self.id+' '+self.name+' '+str(round(self.total()))
i=0
list=[]
for n in range(int(input())):
    id="KH%02d"%(i+1)
    i+=1
    name=input()
    old=int(input())
    new =int(input())
    hieu=new-old
    hd=HoaDon(id,name,hieu)
    list.append(hd)
list.sort(key=lambda x:(-x.total()))
for i in list:
    print(i)

"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""