# -*- coding:utf-8 -*-
import sys
import string
reload(sys)
sys.setdefaultencoding('utf-8')

def is_ascii_digits_char(u):
	if u in string.digits:
		return True
	return False

def is_ascii_letters_char(u):
	if u in string.ascii_letters:
		return True
	return False

def is_ascii_digits_str(s):
	for u in s:
		if not is_ascii_digits_char(u):
			return False
	return True

def is_ascii_letters_str(s):
	for u in s:
		if not is_ascii_letters_char(u):
			return False
	return True

def findDigitEnd(s):
	i = 0
	while i < len(s):
		if not is_ascii_digits_char(s[i]):
			return i
		i += 1
	return i

def findAlphaEnd(s):
	i = 0
	while i < len(s):
		if not is_ascii_letters_char(s[i]):
			return i
		i += 1
	return i

def bigram(content):
	grams = []

	words = []

	terms = []

	i = 0
	max_len = len(content)
	while i < max_len:
		uchar = content[i]
		word = ''
		if is_ascii_digits_char(uchar):
			idx = findDigitEnd(content[i+1:])
			word = content[i:i+1+idx]
			i = i + 1 + idx
		elif is_ascii_letters_char(uchar):
			idx = findAlphaEnd(content[i+1:])
			word = content[i:i+1+idx]
			i = i + 1 + idx
		else:
			word = uchar
			i += 1
		words.append(word)
	#print " ".join(words)

	i = 0
	max_len = len(words)
	while i < max_len:
		word = words[i]
		if i+1 < max_len:
			nex_word = words[i+1]
		else:
			nex_word = None

		if i == 0:
			pre_word = None
		else:
			pre_word = words[i-1]

		if ((pre_word is None) or pre_word.isspace()) and nex_word.isspace():
			grams.append(word)
		elif nex_word is None and (pre_word is None or pre_word.isspace()):
			grams.append(word)
		elif word.isspace():
			pass
		elif (nex_word is not None) and (not nex_word.isspace()):
			grams.append(word + nex_word)
		else:
			pass
		if is_ascii_digits_str(word) or is_ascii_letters_str(word):
			grams.append(word)
		i += 1

	print " ".join(grams)

def unigram(content):
	grams = []

	words = []

	terms = []

	i = 0
	max_len = len(content)
	while i < max_len:
		uchar = content[i]
		word = ''
		if is_ascii_digits_char(uchar):
			idx = findDigitEnd(content[i+1:])
			word = content[i:i+1+idx]
			i = i + 1 + idx
		elif is_ascii_letters_char(uchar):
			idx = findAlphaEnd(content[i+1:])
			word = content[i:i+1+idx]
			i = i + 1 + idx
		else:
			word = uchar
			i += 1
		words.append(word)
	print " ".join(words)

	#print " ".join(grams)



def test_bigram_seg():
	#bigram(u'我是谁XL')
	for line in file(sys.argv[1]):
		bigram(u'' + line.strip().replace(' ', ''))
		pass

def test_unigram_seg():
	for line in file(sys.argv[1]):
		unigram(u'' + line.strip().replace(' ', ''))
		pass

if __name__ == "__main__":
	#test_bigram_seg()
	test_unigram_seg()
