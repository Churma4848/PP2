class Sultan:
    def __init__(self, age, gpa):
        self.age = age
        self.gpa = gpa

    def holdru(self):
        print(f"I am {self.age} years old, and my GPA is {self.gpa}")

p = Sultan(27, 4.0)
p.holdru()

class Student(Sultan):
    def __init__(self, age, gpa, name):
        self.name = "Sultan"
        super().__init__(age, gpa)
        self.name = name
    
c = Student(17, 4.0, Sultan)
print(c.age, c.gpa, c.name)