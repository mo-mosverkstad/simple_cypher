#from hackerLib import isEnglish

letters_low = 'abcdefghijklmnopqrstuvwxyz'

#encrypt = 'oz oy g muuj jge'
encrypt = 'guvf vf zl frperg zrffntr'

# check is english

dic = []

for word in open('english.dic'):
	dic.append(word.rstrip())

def checkEnglish(word):
	if word in dic:
		return True
	else:
		return False

def isEnglish(sentence):
	count = 0
	total = 0
	for word in sentence.split(' '):
		total = total + 1
		if checkEnglish(word):
			count = count + 1
	return count * 1.0000 / total * 100

# hacker Caesar
def hackLetter(l, key):
	index = letters_low.find(l) + key
	if index > 25:
		index = index - 26
	elif index < 0:
		index = index + 26
	return letters_low[index]

def hackString(encryptString, key):
	message = ''
	for l in encryptString:
		if l in letters_low:
			message = message + hackLetter(l, key)
		else:
			message = message + l
	return message

def hackCaesar(encryptString):
	for k in range(0,26):
		decrypt = hackString(encryptString, k)
		print 'key: ' + str(k) + '; the text guess: ' + decrypt + '; isEnglish??? ' + str(isEnglish(decrypt)) + '%'


hackCaesar(encrypt)