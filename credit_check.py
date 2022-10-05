def credit_check(string):
    validCheck=""
    creditArray = []
    for i in range(len(string)):
        creditArray.append(string[i]) 
    for i in range(len(creditArray)):
        if i%2 ==0:
            creditArray[i] = int(creditArray[i]) * 2
        if creditArray[i] > 9:
            sum = 0
            dig = str(creditArray[i])
            for digit in str(creditArray[i]):
                sum += int(digit)
            creditArray[i] = sum
    sum = creditArray[0]
    for i in range(1, len(creditArray)):
        sum = sum + creditArray[i]
    if sum%10 == 0:
        validCheck = "The number is valid!"
    else: 
        validCheck = "The number is invalid!"


    return validCheck

    


# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

