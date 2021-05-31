from random import randrange

def my_choice(data):
    y = randrange(0,len(data))
    return data[y]


print(my_choice([1,2,3,4,5,6,7]))
