def binarySearch(list, num):
    list.sort()
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (high+low)//2
        if list[mid] < num:
            low = mid+1
        elif list[mid] > num:
            high = mid-1
        else: 
            return mid

    return -1

print(binarySearch([4,7,8,12,45,99], 45))