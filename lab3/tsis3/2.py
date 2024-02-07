class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

a = int(input())
if __name__ == "__main__":
    shape = Shape()
    square = Square(a)

    print(shape.area())  
    print( square.area())  