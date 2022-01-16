
class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Calculate(Shape):
    def area(self):
        return self.width * self.height

w = float(input('Please input width: '))
h = float(input('Please input height: '))
calculate = Calculate(w,h)
res = calculate.area()
print('Area :',res)
