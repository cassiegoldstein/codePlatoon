arrayToSearchThrough = []
for i in range(1,1000):
    arrayToSearchThrough.append(i)

def linearSearch(valueToFind, arrayToSearchThrough):
    for i in range(len(arrayToSearchThrough)):
        if arrayToSearchThrough[i]== valueToFind:
            index = i
    print(index)
    return 0


def globalLinearSearch(valueToFind, arrayToSearchThrough):
    arrayOfIndex=[];
    for i in range(len(arrayToSearchThrough)):
        if arrayToSearchThrough[i]==valueToFind:
            arrayOfIndex.append(i)
        
    
    print(arrayOfIndex)
    return 0

linearSearch(6, arrayToSearchThrough)
globalLinearSearch(4, arrayToSearchThrough)