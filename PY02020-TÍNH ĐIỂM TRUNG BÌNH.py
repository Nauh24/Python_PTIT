n=int(input())
a=list(map(float,input().split()))

maxx,minn=max(a),min(a)

s=0
cnt=0
for i in a:
   if i!=maxx and i!=minn:
       s+=i
       cnt+=1
print('{:.2f}'.format(s/cnt))