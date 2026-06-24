# Create a Rectangle class with methods for area and perimeter. 
class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area_f(self):
        return self.length*self.width

newRectangle = rectangle(5, 10)
print(newRectangle.rectangle_area_f())
