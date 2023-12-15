def check(s):
    Sum=0
    for i in s:
        if i.isalpha() or i<'0' or i>'4':
            return 'NO'
        Sum+=int(i)
    if Sum==5: return 'YES'
    else : return 'NO'

for t in range(int(input())):
    s=input()
    print(check(s))

'''
3
1214AB
102101
22222222
'''