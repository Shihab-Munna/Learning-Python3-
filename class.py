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

my_calculator = Calculator()

print(my_calculator.addition(10,12))
print(my_calculator.subtraction(22,20))
print(my_calculator.division(10,2))
print(my_calculator.multipication(11,11))
