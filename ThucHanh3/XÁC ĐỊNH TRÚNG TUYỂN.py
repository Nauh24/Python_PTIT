class GiangVien:
    def __init__(self,id,name,maXetTuyen,tin,chuyenMon):
        self.id=id
        self.name=name
        self.maXetTuyen=maXetTuyen
        self.tin=tin
        self.chuyenMon=chuyenMon
    def mon(self):
        if self.maXetTuyen[0]=='A': return "TOAN"
        if self.maXetTuyen[0]=='B': return "LY"
        return "HOA"
    def uuTien(self):
        if self.maXetTuyen[1]=='1': return 2
        if self.maXetTuyen[1]=='2': return 1.5
        if self.maXetTuyen[1]=='3': return 1
        return 0
    def tongDiem(self):
        return self.tin*2+self.chuyenMon+self.uuTien()
    def status(self):
        if self.tongDiem()>=18: return "TRUNG TUYEN"
        else: return "LOAI"
    def __str__(self):
        return self.id+' '+self.name+' '+self.mon()+' '+'{:.1f}'.format(self.tongDiem())+' '+self.status()

a=[]
i=0
for t in range(int(input())):
    name=input()
    id="GV%02d"%(i+1)
    i+=1
    ma=input()
    tin=float(input())
    cm=float(input())
    gv=GiangVien(id,name,ma,tin,cm)
    a.append(gv)
a.sort(key=lambda x:(-x.tongDiem()))
for i in a:
    print(i)

'''
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''