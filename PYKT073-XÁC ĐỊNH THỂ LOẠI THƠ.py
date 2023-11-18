a=[]
for t in range(int(input())):
    s=input().split()
    a.append(len(s))
cnt1=0
cnt2=0
b=[]
len_tntt=0
for i in a:
    #print(i)
    if i==6 and cnt1==0:
        b.append(1)
        cnt1=1
        cnt2=0
    elif i==7:
        len_tntt+=1
        if cnt2==0: b.append(2)
        cnt1=0
        if len_tntt==4:
            cnt2=0
            len_tntt=0
        else: cnt2=1
print(len(b))
for i in b:
    print(i)
'''
20
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
'''