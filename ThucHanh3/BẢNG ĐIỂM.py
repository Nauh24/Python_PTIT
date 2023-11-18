class SinhVien:
    def __init__(self,id,name,diemTB):
        self.id=id
        self.name=name
        self.diemTB=diemTB
    def status(self):
        if self.diemTB>=9: return 'XUAT SAC'
        if self.diemTB>=8: return 'GIOI'
        if self.diemTB>=7: return 'KHA'
        if self.diemTB>=5: return 'TB'
        return 'YEU'
    def __str__(self):
        return self.id+' '+self.name+' '+str(round((self.diemTB*10.0)/10,1)) +' '+self.status()

a=[]
i=0
for t in range(int(input())):
    id='HS%02d'%(i+1)
    name=input()
    b=[float(j) for j in input().split()]
    diem=sum(b)+b[0]+b[1]
    sv=SinhVien(id,name,diem/12)
    i+=1
    a.append(sv)
a.sort(key=lambda x:(-x.diemTB))
for i in a:
    print(i)

"""
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""