class Calculator:
    def addition (self,a,b):
        return a+b
    def subtraction (self, a, b) :
        return a-b
    def multipication (self, a,b) :
        return a*b
    def division (self ,a ,b ) :
        try:
            return a/b
        except ZeroDivisionError:
            print("It's Impossible to divide by Zero ")

class SuperCalculator (Calculator):
    def squre(self, a):
        return a*a
    def cube(self, a):
        return a*a*a

my_obj = SuperCalculator()

print(my_obj.squre(4))
print(my_obj.cube(2))



