from vector import Vector

class MyVector(Vector):
  def __init__(self, x, y):
    super().__init__(x, y)

  def __eq__(self, other):
      return self.x == other.x and self.y == other.y



def test():
  a = MyVector(1, 2)
  b = MyVector(4, 6)

  #add
  assert a + b == MyVector(5, 8)

  #sub
  assert b - a == MyVector(3, 4)

  #dot
  assert a.dot(b) == 16

  #norm
  assert abs(a.norm() - (a.x ** 2 + a.y ** 2) ** 0.5) < 10e-9

  #repr
  assert repr(a) == "(1, 2)"

  print("Test Passed!!!!")


test()