class Flyable:
    def move(self):
        print("Flying")


class Swimmable:
    def move(self):
        print("Swimming")


class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.move()
