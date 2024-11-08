# Object Oriented Programming Concepts in Python

# Attributes, methods and class

class Humans():
    
    # class object attribute
    # same for any instance of a class
    species = 'Homo Sepians'

    # Default constructor method of class called automatically after instance(object) creation
    def __init__(self,color,name,car):
        #Attributes. We take in arguments. Assign it using self.attribute_name
        #self = instance of a class
        self.color = color
        self.name = name
        self.car = car

    # methods    
    def car_num(self,num):
        print("hey my name is {} and my car number is {}".format(self.name,num))

fav_car_obj=Humans(color='blue',name='uday',car='Jaguar') #creating instance or object for class
print(fav_car_obj.species) # accessing the variable
print("hey\t" +fav_car_obj.name + "\thas\t" + fav_car_obj.color + "\tcolor\t" + fav_car_obj.car)
fav_car_obj.car_num(3)


# Inheritance 
  ## Uses: Ability to resue code
          #Reduce the complexity of the code

class CookeryPortal():
    def __init__(self):
        print("this is a portal where new chefs can refer recipes")
    def recipes(self,name):
        print("These are the recipes {}".format(name))
class Chef(CookeryPortal):
    def __init__(self):
        CookeryPortal.__init__(self)
        print("this is chef boundary")
mychef = Chef()
mychef.recipes('chicken')




# Polymorphism
class Friend1():
    def __init__(self,name):
        self.name = name
    def fav_color(self):
        return self.name + 'blue'
class Swetha():
    def __init__(self,name):
        self.name = name
    def fav_color(self):
        return self.name + "black"
uday_obj = Uday('')