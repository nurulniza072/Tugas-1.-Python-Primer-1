def is_even(k):
    if k == 0 :
        return ("TRUE");
    elif k == 1:
        return ("FALSE");
    else:
        return is_even(k-2)


print(is_even(101))
