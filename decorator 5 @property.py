class MyClass:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

if __name__ == "__main__":

    obj = MyClass('Shihab','Munna')
    print(obj.full_name)
    obj.full_name = "New Name"
# @property makes a class as readonly  .

