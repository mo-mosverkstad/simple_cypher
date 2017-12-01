def reverse(plainText):
	chiffer = ''
	for i in range(len(plainText)-1,-1,-1):
		chiffer = chiffer + plainText[i]
	return chiffer

def encRev(plainText):
	return reverse(plainText)

def decRev(plainText):
	return reverse(plainText)

print reverse(raw_input('reversed cipher:>'))