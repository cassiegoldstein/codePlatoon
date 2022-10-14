def translate(word):
    phrase = word.split()
    newPhrase = []
    vowels = 'AEIOUaeiou'
    consonents = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
    for i in range(len(phrase)):
        if phrase[i][0] in vowels:
            newWord = "".join(phrase[i]+"ay")
            newPhrase.append(newWord)
        elif phrase[i][0] in consonents:
            newWord = phrase[i][1:]
            newWord = "".join(newWord+phrase[i][0]+"ay")
            newPhrase.append(newWord)
    print(" ".join(newPhrase))



translate("Hi my name is Cassie Goldstein")