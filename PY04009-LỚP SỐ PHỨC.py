class soPhuc:
    def __init__(self,thuc,ao):
        self.thuc=thuc
        self.ao=ao
    def __add__(self, other):
        t=self.thuc+other.thuc
        a=self.ao+other.ao
        return soPhuc(t,a)
    def __mul__(self, other):
        t=self.thuc*other.thuc-self.ao*other.ao
        a=self.thuc*other.ao+self.ao*other.thuc
        return soPhuc(t,a)
    def __str__(self):
        if self.ao<0: return f'{self.thuc} - {self.ao*-1}i'

        return f'{self.thuc} + {self.ao}i'
for t in range(int(input())):
    x,y,z,t=map(int,input().split())
    a,b=soPhuc(x,y),soPhuc(z,t)
    c=(a+b)*a
    d=(a+b)*(a+b)
    print(c,d,sep=', ')
    print()

"""
3
1 2 3 4
2 3 4 5
1 -2 5 -6
"""