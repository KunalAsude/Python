import math
def cal(r):
    area = math.pi * r**2
    cir = 2* math.pi*r
    return area , cir

a,c=cal(4)
print('area is - ',round(a,2))
print("circumference -",round(c,2))