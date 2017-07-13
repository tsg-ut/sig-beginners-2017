class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)

    def dot(self,other):
        return self.x * other.x + self.y * other.y

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)