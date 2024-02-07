class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

a = int(input())
b = int(input())
if __name__ == "__main__":
    rectangle = Rectangle(a, b)

    print( rectangle.area())  
