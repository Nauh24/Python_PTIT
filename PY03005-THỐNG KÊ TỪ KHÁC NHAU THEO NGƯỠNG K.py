import re
n,k=map(int,input().split())
s=''
for i in range(n):
    line=input()
    s+=line+' '
s=s.strip().lower()
s=re.split("[^a-z0-9]",s)
s=[x for x in s if x]
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
d=sorted(d.items(),key=lambda x: (-x[1],x[0]))
for i in d:
    if i[1]>=k:
        print(i[0],i[1])
'''
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
'''