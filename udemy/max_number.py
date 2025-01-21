#Problem statemet: Find out max number from a list

def max_number(num_list):
    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

result = max_number([8,2,55,8,12])
print('max number is: ' + str(result))
