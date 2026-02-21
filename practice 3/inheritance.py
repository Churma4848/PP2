class Sultan:
    def __init__(self, age, gpa):
        self.age = age
        self.gpa = gpa

    def holdru(self):
        print("I am " + self.age +"years old, and my GPA is" + self.gpa)

p = Sultan(27, 4.0)
p.holdru()

class Student(Sultan):
    pass