# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	list1 = list(string1)
	list1.sort()
	list2 = list(string2)
	list2.sort()
	if (list1 == list2):
		return True
	else:
		return False
	pass


# Part 2
def anagrams_for(word, list_of_words):
	listWord = list(word)
	listWord.sort()
	newList = list()
	for i in range(len(list_of_words)):
		listI = list(list_of_words[i])
		listI.sort()
		if listI == listWord:
			newList.append(list_of_words[i])
	return newList
