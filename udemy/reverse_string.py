# Problem statement: I have to define a function and it should take input string and reverse it

def my_reverse(rev):
    reverse_str=rev[::-1] #slicing 
    #print('reversed string:' + reverse_str)
    return reverse_str

result = my_reverse("uday")
print('reversed string: ' + result)