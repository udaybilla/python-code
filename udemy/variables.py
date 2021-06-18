# Variables are like containers used to store the data values.

# Note - unlike other programming languages python does not have any command to declare variables.

'''
Rules for variables:
 - must start with a letter or the underscore character
 - cannot start with a number
 - can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
 - names are case-sensitive (age, Age and AGE are three different variables)
'''


#strings
import json
my_income = 89773
tax = 0.9
total_income = my_income * tax
print(total_income)

mystring = 'Hello uday'
print(mystring[6:])
print(mystring.upper())



#printing fizz and buzz for numbers
def fizz_buzz():
    i = 0
    for i in range(1,100):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        else:
            print(i)
fizz_buzz()


# Note - Variables do not need to be declared with any particular type, and can even change type after they have been set in python.
x = 2 # x is int type here it is changed to string in the next line
x = 'changed to string' 
x = "changed to string" #string can be double quoted or single quoted

# Assign values to multiple varibales in single line, you can assign the same value to multiple variables in one line:
my_name, my_wife , my_car = 'uday', "sony", 'Honda Accord'
print("me {} and my wife {} drive {}".format(my_name,my_wife,my_car))
my_car = deepak_car = anne_car = 'Honda Accord'


'''
Global Variables: 
- Variables created outside a function are global
- can be used by everyone both inside and outside of functions.
'''
x = 'welcome'
def my_welcome():
    print('Hello uday {}'.format(x))
my_welcome()

'''
Local Varibales and Global keyword:
- when you create a variable inside a function, that variable is local, and can only be used inside that function.
- To create a global variable inside a function, you can use the global keyword.
'''
my_brother = 'shashi' #global variable
my_sis = 'sahitya'
def cousin():
    my_brother = 'pranay' #local variable
    global my_aunt 
    my_aunt = 'nirmala' # creating global variable inside the function.
    global my_sis # Refering global variable in the function to change its value.
    my_sis = 'ashrita' 
    print('He is my cousin {}'.format(my_brother))
cousin()


