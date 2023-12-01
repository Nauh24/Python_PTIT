import re


n=int(input())
s=''
for i in range(n):
    line=input()
    s+=line+' '
s=s.lower().strip()    
s=re.split("[^a-z0-9]",s.strip())

d={}
for i in s:
    if i not in d:
        d[i]=1
    else: d[i]+=1
c=sorted(d.items(),key=lambda x: (-x[-1],x[0]))
ok=set()
for i in c:
    res='{} {}'.format(i[0],i[1])
    if res not in ok:
        print(res)
        ok.add(res)



#print(*a)
'''
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
'''