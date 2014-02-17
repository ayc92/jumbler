import sys

WORD_LIST = set()

def populate_word_list(filename):
	with open(filename, 'ru') as f:
		for line in f:
			WORD_LIST.add(line.rstrip())

def find_jumbles_dispatcher(word):
	letters_set = {}
	jumbles = []
	for letter in word:
		if letter in letters_set:
			letters_set[letter] += 1
		else:
			letters_set[letter] = 1
	for letter in word:
		letters_set[letter] -= 1
		jumbles += find_jumbles(letter, letters_set)
		letters_set[letter] += 1
	return jumbles

def find_jumbles(current_word, letters_left):
	word_lst = []
	if current_word in WORD_LIST:
		word_lst.append(current_word)
	for letter in letters_left:
		if letters_left[letter] > 0:
			letters_left[letter] -= 1
			word_lst += find_jumbles(current_word + letter, letters_left)
			letters_left[letter] += 1
	return word_lst

if __name__ == "__main__":
	populate_word_list(sys.argv[1])
	print find_jumbles_dispatcher(sys.argv[2])
