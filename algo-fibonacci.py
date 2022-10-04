def fibonacci(num):
    
    num1 = 0
    num2 = 1
    if (num<2):
        print(num)

    else:
        for i in range(num):
            fib = num1 + num2
            num1 = num2
            num2 = fib
            i = i + 1

        print(fib)

fibonacci(5)