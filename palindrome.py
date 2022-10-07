def palindrome(word):
    testWord = str(word)
    reverseWord = testWord[::-1]
    if reverseWord == testWord:
        return(True)
    else: 
        return(False)

print(palindrome("mom"))

