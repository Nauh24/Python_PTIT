for t in range(int(input())):
    print('Test '+str(t+1)+': ',end='')
    s1=input()
    s2=input()
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print('YES')
    else:
        print('NO')
'''
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
'''