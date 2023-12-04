class GiangVien:
    def __init__(self,id,name,maXetTuyen,tin,cm):
        self.id=id
        self.name=name
        self.maXetTuyen=maXetTuyen
        self.tin=tin
        self.cm=cm
    def mon(self):
        if self.maXetTuyen[0]=='A': return 'TOAN'
        elif self.maXetTuyen[0]=='B': return 'LY'
        else: return 'HOA'
    def uuTien(self):
        if self.maXetTuyen[1]=='1': return 2
        elif self.maXetTuyen[1]=='2': return 1.5
        elif self.maXetTuyen[1]=='3': return 1
        else : return 0
    def tongDiem(self):
        return self.tin*2+self.cm+self.uuTien()
    def status(self):
        if self.tongDiem()>=18: return 'TRUNG TUYEN'
        else : return 'LOAI'
    def __str__(self):
        return self.id+' '+self.name+' '+self.mon()+' '+'{:.1f}'.format(self.tongDiem())+' '+self.status()
    
n=int(input())
a=[]
for i in range(n):
    id='GV%02d'%(i+1)
    name=input()
    ma=input()
    tin=float(input())
    cm=float(input())
    gv=GiangVien(id,name,ma,tin,cm)
    a.append(gv)
a.sort(key=lambda x: -x.tongDiem())
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