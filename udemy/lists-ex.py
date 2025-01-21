def merge(lst1, lst2):
    # Write code here
    for i in range(len(lst2)):
        lst1.append(lst2[i])
    lst1.sort()
    print(lst1)
    return lst1
    

merge([3, 2, 8], [5, 4, 6])