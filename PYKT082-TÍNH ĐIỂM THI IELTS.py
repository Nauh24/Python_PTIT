def trans(x):
    if x>=39: return 9
    if x>=37: return 8.5
    if x>=35: return 8
    if x>=33: return 7.5
    if x>=30: return 7
    if x>=27: return 6.5
    if x>=23: return 6
    if x>=20: return 5.5
    if x>=16: return 5
    if x>=13: return 4.5
    if x>=10: return 4
    if x>=7: return 3.5
    if x>=5: return 3
    if x>=3: return 2.5
for t in range(int(input())):
    a,b,c,d=map(float,input().split())
    s=(trans(a)+trans(b)+c+d)/4
    if s-int(s)>=0.75: s=int(s)+1
    elif s-int(s)>=0.25: s=int(s)+0.5
    else: s=int(s)
    print('{:.1f}'.format(s))
'''
2
15 25 5.0 5.5
22 32 6.0 6.0
'''