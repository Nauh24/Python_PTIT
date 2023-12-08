class CaThi:
    def __init__(self,id,ngayThi,gioThi,phongThi):
        self.id=id
        self.ngayThi=ngayThi
        self.gioThi=gioThi
        self.phongThi=phongThi
    def time(self):
        s=list(self.ngayThi.split('/'))
        x=list(self.gioThi.split(':'))
        res=s[2]+s[1]+s[0]+x[0]+x[1]+self.id
        return res
    def __str__(self):
        return self.id+' '+self.ngayThi+' '+self.gioThi+' '+self.phongThi

file=open('CATHI.in','r')
a=[]
for i in range(int(file.readline())):
    id="C%03d"%(i+1)
    ngaythi=file.readline().strip()
    giothi=file.readline().strip()
    phongthi=file.readline().strip()
    ct=CaThi(id,ngaythi,giothi,phongthi)
    a.append(ct)

a.sort(key=lambda x: x.time())
for i in a:
    print(i)
'''
2
09/01/2022
15:30
70172
09/01/2022
10:00
70279
'''