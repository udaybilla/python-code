## Converting data types from one to another int --> str
## Implicit (Automatic), Explicit (manual)

# Example where implicit type conversion happend automatically if you see below.
my_lucky_num = 3
my_income = 140000.32

my_new_income = my_lucky_num + my_income

print("my new income would be: ", my_new_income)


# Explicit type casting

my_birth_day = '1'
my_lucky_number = 3

#now i need to explicit conversion to get the diff between them

my_actual_birth_date = int(my_birth_day)
diff = my_lucky_num - my_actual_birth_date

print("Difference would be", diff)