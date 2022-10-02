def deaf_grandma():
    byeCount = 0
    x = input('HEY KID!' )
    while byeCount < 1:
        if len(x) == 0:
            print('WHAT!?')
        elif x == 'GOODBYE!':
            byeCount = byeCount + 1
            print("LEAVING SO SOON?")
        elif x.isupper() == True:
            print('NO, NOT SINCE 1946!')
        else:
            for character in x:
                if character.islower():
                    print('SPEAK UP, KID!')
                    break
        x = input()

deaf_grandma()
