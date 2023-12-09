
class ThiSinh:
    def __init__(self,id,name,diemThi,danToc,khuVuc):
        self.id=id
        self.name=name
        self.diemThi=diemThi
        self.danToc=danToc
        self.khuVuc=khuVuc
    def diemUuTien(self):
        diem=0
        if self.khuVuc=='1': diem+=1.5
        if self.khuVuc=='2': diem+=1
        if self.danToc!='Kinh': diem+=1.5
        return diem
    def tongDiem(self):
        return self.diemThi+self.diemUuTien()
    def status(self):
        d=self.tongDiem()
        if d>=20.5: return 'Do'
        else: return 'Truot'
    def chuanHoa(self):
        ans=self.name.split()
        return ' '.join(ans).title()
    def __str__(self):
      
        return self.id+' '+self.chuanHoa()+' '+str('{:.1f}'.format(self.tongDiem()))+' '+self.status()
    
n=int(input())
a=[]
for i in range(n):
    id="TS%02d"%(i+1)
    name=input()
    diemThi=float(input())
    dtoc=input()
    kvuc=input()
    ts=ThiSinh(id,name,diemThi,dtoc,kvuc)
    a.append(ts)
a.sort(key= lambda x:(-x.tongDiem(),x.id))
for i in a:
    print(i)
'''
2
  Chu thi MINh
14
Dao
3
Nguyen  hong ngat
22
Kinh
1

'''
