from PyDictionary import PyDictionary

dictionary = PyDictionary()
Word = (input("Enter a word: "))
meaning = dictionary.meaning(word)
for i in meaning:
	print(f'{i} = {meaning[i]}')
	print('')


