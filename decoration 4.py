class My_class:
    def __init__(self):
        pass
    def square(self,x):
        return x**2
    @staticmethod
    def cube(x):
        return x**3

if __name__ == "__main__":
    m = My_class()

    print(m.square(3))
    print(m.cube(3))
    print(My_class.cube(3))
    print(My_class.square(3))


