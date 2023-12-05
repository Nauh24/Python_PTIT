class MonHoc:
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        self.type=type
    def __str__(self):
        return self.id+ ' '+self.name+' '+self.type
n=int(input())
a=[]
for i in range(n):
    id=input()
    name=input()
    type=input()
    mh=MonHoc(id,name,type)
    a.append(mh)
a=sorted(a,key=lambda x: x.id)
for i in a:
    print(i)
'''
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
'''