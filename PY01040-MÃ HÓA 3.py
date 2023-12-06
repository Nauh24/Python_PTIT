# def rotate(s):
def rotate(s):
    Sum=0
    for i in s:
        Sum+=ord(i)-ord('A')
    res=''
    for i in s:
        res+=chr((ord(i)-ord('A')+Sum)%26+ord('A'))
    return res
def merge(a,b):
    res=''
    for i in range(len(a)):
        res+=chr((ord(a[i])+ord(b[i]))%26+ord('A'))
    return res
for t in range(int(input())):
    s=input()
    #devide
    n=len(s)
    a=s[:(n//2)]
    b=s[(n//2):]

   #rotate
    x=rotate(a)
    y=rotate(b)
    #merge
    print(merge(x,y))

'''
3
EWPGAJRB
BB
TPQJDRJWSQXGRRIPXFMINTELHBJA
'''