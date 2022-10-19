def bottleSong(numBottle):
    print(str(numBottle)+ " bottles of beer on the wall, " + str(numBottle)+ " bottles of beer, " + "take one down and pass it around, " + str(numBottle-1)+ " bottles of beer on the wall.")
    if numBottle == 0:
        return 0
    else:
        return bottleSong(numBottle-1)
  
bottleSong(10)