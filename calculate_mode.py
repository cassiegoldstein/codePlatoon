from collections import Counter

def calculate_mode(list):
    counter = Counter(list)
    list_vals =[]
    x = counter.most_common()
    max_occurance = x[0][1]
    list_vals.append(x[0][0])
    for i in range(1, len(x)):
        if x[i][1] >= max_occurance:
            list_vals.append(x[i][0])

    return list_vals



  
 
list = [2, 1, 2, 2, 1, 2, 3, 4, 3, 3, 3]
print(calculate_mode(list))
