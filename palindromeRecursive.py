def palindrome(word):
    if len(word) < 2 or word[0] == word[-1]:
        return True
    else:
        palindrome(word[1:-1])
    return False


print(palindrome("madam"))
