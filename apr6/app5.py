
class Shape:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self.x, self.y = kwargs.pop('x'), kwargs.pop('y')
        super().__init__(*args, **kwargs)


class ColoredObject:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self.color = kwargs.pop('color')
        super().__init__(*args, **kwargs)


class ColoredCircle(Shape, ColoredObject):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self.r = kwargs.pop('r')
        super().__init__(*args, **kwargs)


class Coloredtriangle(ColoredObject, Shape):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self.a = kwargs.pop('a')
        super().__init__(*args, **kwargs)



c = Coloredtriangle(x=1, y=2, color=3, a=4)
print("----------------------")
d = ColoredCircle(x=1, y=2, color=3, r=4)