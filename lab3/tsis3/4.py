import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if __name__ == "__main__":
    point1 = Point(a, b)
    point2 = Point(c, d)

    point1.show()  
    point2.show() 

    distance = point1.dist(point2)
    print(f"Distance between points: {distance}")  

    point1.move(e, f)
    point1.show() 
