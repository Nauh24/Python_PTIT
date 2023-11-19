n=int(input())
d=dict()
key=''
for _ in range(n):
    s=input()
    if key=='':
        key=s
        d[key]=0
    elif s!='':
        d[key]+=1
    else:
        key=''
for i in d:
    print(f'{i}: {d[i]}')

'''
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
'''
