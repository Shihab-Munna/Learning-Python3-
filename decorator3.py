class my_class:
    def __init__(self):
        pass
    @classmethod
    def squre(self,x):
        return x**2
    @classmethod
    def cube(self,x):
        return x**3

if __name__ == "__main__":
    m = my_class()
print(m.squre(3))
print(m.cube(3))
print(my_class.cube(3))
print(my_class.squre(3))
# You can call a mathod both calling by object or calling useing his class name .