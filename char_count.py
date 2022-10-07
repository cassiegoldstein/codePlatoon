from collections import Counter

def char_count(string):
  character_list = []
  counter = Counter(string)
  x = counter.most_common()
  for i in range(len(x)):
    if x[i][0] != " ":
        character_list.append(list(x[i]))
  for i in range(1, len(character_list)):
    if character_list[i][1] == character_list[i-1][1]:
      if character_list[i-1][0] > character_list[i][0]:
        character_list[i-1], character_list[i] = character_list[i], character_list[i-1]
  return(character_list)

string = "an apple a day keeps the doctor away"
print(char_count(string))
