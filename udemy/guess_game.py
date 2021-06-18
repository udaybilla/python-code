# Game for user random guess of string 'blue' position  in list
# Interaction between functions takes place in this game project 

from random import shuffle

#shuffle the list
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
    
#inout of user function
def user_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("please pick a number to guess your favourite colour: 0,1, or 2")
    return int(guess)

#checking the guess
def check_guess(my_list,guess):
    if my_list[guess] == 'Blue':
        print("hey you picked your favourite colour" + my_list[guess])
    else:
        print("Sorry wrong guess! you picked " + my_list[guess])
        print(my_list)

#Initial list of colours
my_list = ['Blue','Green','Yellow']

#shuffle list
mixedup_list = shuffle_list(my_list)

#user guess
guess = user_guess()

#check guess
check_guess(mixedup_list,guess)