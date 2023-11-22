
s=input()
cnt=0

while len(s)>1:
    tong=0
    tong=sum(int(i) for i in s)
    #for i in s: tong+=ord(i)-ord('0')
    s=str(tong)
    cnt+=1
print(cnt)