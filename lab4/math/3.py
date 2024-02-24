import math

def polygon(n, a):
    area = (n * a**2 ) / (4 * math.tan(math.pi / n))
    return area

n = int(input())
a = int(input())

area = polygon(n, a)
print(area)