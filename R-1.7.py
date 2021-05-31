def odd_squares_sum(n):
    return sum(y*y for y in range(0,n)
               if y%2==1)


print(odd_squares_sum(8))
