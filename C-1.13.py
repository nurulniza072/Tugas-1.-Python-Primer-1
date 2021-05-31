def reverse_list_of_integers(list):
    reversed_array=[]
    for y in range(0, len(list)):
        reversed_array.append(list[len(list)-y-1])
    return reversed_array

print(reverse_list_of_integers([6,7,8,9,10]))
