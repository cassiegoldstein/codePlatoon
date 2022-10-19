def bubbleSort(list):
    #iterate backwards over length of list minus one. i.e. if list is length of 5, iterates from 4-1
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            #current = list[j+1]
            #previous = list[j]
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

            

        





list = [4, 3, 5, 0, 1]
print(bubbleSort(list))


