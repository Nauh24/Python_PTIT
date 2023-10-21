list=[]
for i in range(int(input())):
    x=input()
    y,z=map(int,input().split())
    list.append((x,y,z))
list.sort(key=lambda x: x[0])
list.sort(key=lambda x: x[2])
list.sort(key=lambda x: x[1],reverse=True)
for i in list:
    print(*i)

'''
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
'''