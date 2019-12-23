class Calcu:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def devition(self):
        try:
            return self.a /self.b
        except ZeroDivisionError:
            print("Can't Divide any thing by 0")

class SuperCalculator (Calcu):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def add (self):
        return self.a + self.b + self.c

cal = SuperCalculator(10,11,10)

print(cal.add())

