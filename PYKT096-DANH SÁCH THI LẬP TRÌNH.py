class Team:
    def __init__(self,ma,tenTeam,tenTruong):
        self.ma=ma
        self.tenTeam=tenTeam
        self.tenTruong=tenTruong

class ThiSinh:
    def __init__(self,ma,ten,team: Team):
        self.ma=ma
        self.ten=ten
        self.team=team
    def __str__(self):
        return self.ma+' '+self.ten+' '+self.team.tenTeam+' '+self.team.tenTruong
a=[]
d={}
for i in range(int(input())):
    ma="Team%02d"%(i+1)
    tenTeam=input()
    tenTruong=input()
    d[ma]=Team(ma,tenTeam,tenTruong)
for i in range(int(input())):
    ma="C%03d"%(i+1)
    ten=input()
    maTeam=input()
    ts=ThiSinh(ma,ten,d[maTeam])
    a.append(ts)
a.sort(key=lambda  x: x.ten)
for i in a:
    print(i)

'''
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
'''