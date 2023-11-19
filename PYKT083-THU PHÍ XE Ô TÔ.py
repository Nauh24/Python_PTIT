def chiphi(loaixe, soghe):
    if loaixe == 'Xe_con' and soghe == 5:
        return 10000
    if loaixe == 'Xe_con' and soghe == 7:
        return 15000
    if loaixe == 'Xe_tai' and soghe == 2:
        return 20000
    if loaixe == 'Xe_khach' and soghe == 29:
        return 50000
    if loaixe == 'Xe_khach' and soghe == 45:
        return 70000

a = {}
for t in range(int(input())):
    inputs = input().split()

    bienso = inputs[0]
    loaixe = inputs[1]
    socho = int(inputs[2])
    huong = inputs[3]
    ngay = inputs[4]

    if huong == 'IN':
        if ngay in a:
            a[ngay] += chiphi(loaixe, socho)
        else:
            a[ngay] = chiphi(loaixe, socho)

for i in a:
    print(f'{i}: {a[i]}')






'''
5
30F-123.15 Xe_con 5 OUT 06/11/2021
30F-123.15 Xe_con 5 IN 06/11/2021
30H-123.15 Xe_con 7 IN 06/11/2021
29H-222.68 Xe_tai 2 IN 07/11/2021
30G-511.15 Xe_con 5 IN 07/11/2021
'''