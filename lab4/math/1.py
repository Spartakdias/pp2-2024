import math

def deg(n):
    rad = n * (math.pi / 180)
    return rad

degree = float(input())

radian = deg(degree)
print(radian)