class Student:
    def __init__(self,name,bd,d1,d2,d3):
        self.name=name
        self.bd=bd
        self.d1=d1
        self.d2=d2
        self.d3=d3
    def sum(self):
        return self.d1+self.d2+self.d3
    def __str__(self):
        return f'{self.name} {self.bd} {self.sum()}'
name=input()
bd=input()
d1=float(input())
d2=float(input())
d3=float(input())
print(Student(name, bd, d1, d2, d3))

"""
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
"""