def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([103,4,5,26,2,21,33,98,4,52,5,35,2,-101]))
