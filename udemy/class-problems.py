
class MyDetails:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

my_obj = MyDetails("uday", 37)
my_obj.display()