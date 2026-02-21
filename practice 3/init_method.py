class Sultan:
  def __init__(self, unis, sat):
    self.unis = unis
    self.sat = sat

p1 = Sultan("KBTU", 1560)

print(p1.unis)
print(p1.sat)

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)