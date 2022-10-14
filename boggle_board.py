import string
import random

# class BoggleBoard:


#   def __init__(self):
#     self.game_board = ['_'] * 16

#   def shake(self):
#     pass

#   def view_game_board(self):
#     for i in range(0, len(self.game_board), 4):
#       print("".join(self.game_board[i:i+4]))



  

# boggle= BoggleBoard()
# boggle.view_game_board()

class BoggleBoard:
  
  def __init__(self):
    self.arr = []
    self.rows = 4
    self.cols = 4
    self.dice = [
      'AAEEGN',
      'ELRTTY',
      'AOOTTW',
      'ABBJOO',
      'EHRTVW',
      'CIMOTU',
      'DISTTY',
      'EIOSST',
      'DELRVY',
      'ACHOPS',
      'HIMNQU',
      'EEINSU',
      'EEGHNW',
      'AFFKPS',
      'HLNNRZ',
      'DEILRX'
    ]
    self.allWords = []

  def shake(self):
    toShake = "y"
    while toShake == "y":
      self.arr = []
      random.shuffle(self.dice)
      for i in range(self.rows):
        row = []
        for j in range(self.cols):
         value = random.choice(self.dice[i])
         if value == "Q":
            row.append("Qu")
         else:
            row.append(value)
        self.arr.append(row)
      for row in self.arr:
       print(" ".join(row))
      toShake = input("Would you like to shake your board? (y/n)")
    return self.arr

  def collect_all_words(self):
    diag1 = []
    diag2 = []
    for i, row in enumerate(self.arr):
      self.allWords.append("".join(row))
      reverseHorizontal = row[::-1]
      column_word =[]
      self.allWords.append("".join(reverseHorizontal))
      for j, char in enumerate(row):
        if i == j:
          diag1.append(char)
        elif i+j == 3:
          diag2.append(char)
        column_word.append(self.arr[j][i])
      self.allWords.append("".join(column_word))
      self.allWords.append("".join(column_word[::-1]))
    self.allWords.append("".join(diag1))
    self.allWords.append("".join(diag1[::-1]))
    self.allWords.append("".join(diag2))
    self.allWords.append("".join(diag2[::-1]))
    return self.allWords


  def includeWord(self, word):
    self.collect_all_words()
    if word in self.allWords:
      return True
    else:
      return False 


boggleGame = BoggleBoard()
start = input("Would you like to start a game of Boggle? (y/n)")
if start == "y":
  boggleGame.shake()
  boggleGame.collect_all_words()
  print(boggleGame.includeWord("GANG"))


