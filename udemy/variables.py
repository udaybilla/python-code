'''import json
my_income = 89773
tax = 0.9
total_income = my_income * tax
print(total_income)

mystring = 'Hello uday'
print(mystring[6:])
print(mystring.upper())'''



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