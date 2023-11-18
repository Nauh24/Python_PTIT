class Contact:

    def __init__(self,name,phone,date):
        self.name=name
        self.phone=phone
        self.date=date
        l=self.name.split()
        self.hodem=''
        self.ten=l[-1]
        for i in range(len(l)-1):
            self.hodem+=l[i]+' '
    def __str__(self):
        return '{}: {} {}'.format(self.name,self.phone,self.date)

f=open('SOTAY.txt','r')
a=[]
current_date=None
while True:
    line=f.readline().strip()
    if not line:
        break
    if line.startswith('Ngay '):
        current_date=line[5:]
    else:
        name=line
        phone=f.readline().strip()
        a.append(Contact(name,phone,current_date))
f.close()
a.sort(key=lambda x: (x.ten,x.hodem))
f2=open('DIENTHOAI.txt','w')
for i in a:
   f2.write(str(i)+'\n')
f2.close()







