# Practicing methods and functions
''' 
   key difference between methods and functions in python
   --> Functions are independent and can be called by only its name
   --> methods are dependent on class and should be called by class object
'''

# Functions
def my_name():
    print("hello")
my_name()

#Function with a parameter and a default value
def my_name2(username='uday'):
    print("hello world my name is " +username)
my_name2("ubilla")
my_name2()

#Function with return
def multipy_numbers(a,b):
    #return do not print the output to the console
    #print(a*b)
    result = a*b
    return result
multipy_numbers(2,3)

#Function with operators and statements, loops
def odd_numbers_check(num_list):
    #check for odd numbers in the list and add it to the new list

    #placeholder variable
    odd_numbers=[]
    for number in num_list:
        if number % 2 != 0:
            odd_numbers.append(number)
        else:
            pass
    print(odd_numbers)
    return odd_numbers
odd_numbers_check([1,2,4,3,7,8,12])

#Function with multiple arguments
def my_multiple_args(*args):
    # *args stores arguments in tuple 
    #print (sum(args))
    return sum(args) * 0.10
my_multiple_args(20,30,40)

# Combination of *args and *kwargs in Function
def diff_argunments(*args, **kwargs):
    # kwarags are stored in Dictinonary 
    # Note: args and kwargs should be mentioned in order which they are declared in function
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['shoes']))
diff_argunments('blue','green','yellow',shoes='nike',dress='us polo t shirt',watch='apple')


