def factorial(num):
    fact = 1
    for i in range(num):
        fact = fact * (num-i)
        i = i + 1
    print(fact)


factorial(4)