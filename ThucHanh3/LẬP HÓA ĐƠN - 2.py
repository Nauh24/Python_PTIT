from datetime import datetime


class Customer:
    def __init__(self,id,name,soPhong,ngayDen,ngayDi,phiPhatSinh):
        self.id=id
        self.name=name
        self.soPhong=soPhong
        self.days=str(datetime.strptime(ngayDi,'%d/%m/%Y')-datetime.strptime(ngayDen,'%d/%m/%Y')).split()[0]
        if self.days=='0:00:00' : self.days=1
        else : self.days=int(self.days)+1
        self.phiPhatSinh=phiPhatSinh
    def donGia(self):
        x=self.soPhong[0]
        if x=='1': return 25
        if x=='2': return 34
        if x=='3': return 50
        return 80
    def tong(self):
        return self.donGia()*self.days+self.phiPhatSinh
    def __str__(self):
        return self.id+' '+self.name+' '+self.soPhong+' '+str(self.days)+' '+str(self.tong())
a=[]
i=0
for t in range(int(input())):
   id='KH%02d'%(i+1)
   name=input()
   soPhong=input()
   ngayDen=input().strip()
   ngayDi=input().strip()
   phiPhatSinh=int(input())
   c=Customer(id,name,soPhong,ngayDen,ngayDi,phiPhatSinh)
   i+=1
   a.append(c)
a.sort(key=lambda x:(-x.tong()))
for i in a:
    print(i)

"""
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
"""
