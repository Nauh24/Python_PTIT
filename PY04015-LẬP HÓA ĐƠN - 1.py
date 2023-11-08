class HoaDon:
    def __init__(self,id,name,hieuChiSo):
        self.id=id
        self.name=name
        self.hieuChiSo=hieuChiSo


    def total(self):
        if self.hieuChiSo<=50: return self.hieuChiSo*100+self.hieuChiSo*100*0.02
        elif self.hieuChiSo<=100: return self.hieuChiSo*150*0.03+self.hieuChiSo*150
        else:return self.hieuChiSo*200*0.05+self.hieuChiSo*200
    def __str__(self):
        return self.id+' '+self.name+' '+str(self.total())
i=1
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