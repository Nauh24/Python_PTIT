import math
class Fract:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def rutGon(self):
        x=math.gcd(self.tu,self.mau)
        self.tu//=x
        self.mau//=x
        return '{}/{}'.format(self.tu,self.mau)

a,b=map(int,input().split())
f=Fract(a,b)
print(f.rutGon())