
def bottleSong(num):
    while (num >= 0):
        if (num == 2):
            print(str(num)+" bottles of beer on the wall, "+str(num)+" bottles of beer. Take one down and pass it around, ")
            num=num-1
            print(str(num)+" bottle of beer on the wall.")
        elif (num == 1):
            print(str(num)+' bottle of beer on the wall, '+str(num)+' bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.')
            num=num-1
        elif (num == 0):
            print('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')
            num=num-1
        else:
            print(str(num)+' bottles of beer on the wall, '+str(num)+' bottles of beer. Take one down and pass it around, ')
            num=num-1
            print(str(num) +' bottles of beer on the wall.')
  
  
bottleSong(5)