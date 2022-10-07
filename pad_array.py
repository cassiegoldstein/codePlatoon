def pad(array, min_size, value = None):
    if len(array) == min_size:
        return array
    else:
        for i in range(min_size-(len(array))):
            array.append(value)
        return array


print(pad([1,2,3], 5, 'apple'))