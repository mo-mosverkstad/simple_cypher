alphabet = 'abcdefghijklmnopqrstuvwxyz'
mapping = [5, 21, 14, 23, 0, 11, 18, 9, 2, 4, 7, 15, 25, 16, 1, 8, 12, 20, 3, 6, 10, 13, 17, 19, 22, 24]


def encryptletter(l):
	if l in alphabet:
		i = alphabet.index(l)
		encIndex = mapping[i]
		return alphabet[encIndex]
	else:
		return l

def encryptMapping(s):
	encrypt = ''
	for l in s:
		if l.islower():
			encl = encryptletter(l)
		else:
			encl = encryptletter(l.lower())
			encl = encl.upper()
		encrypt = encrypt + encl
	return encrypt

def decryptletter(l):
	if l in alphabet:
		i = alphabet.find(l)
		decIndex = mapping.index(i)
		return alphabet[decIndex]
	else:
		return l

def decryptMapping(s):
	decrypt = ''
	for l in s:
		if l.islower():
			decl = decryptletter(l)
		else:
			decl = decryptletter(l.lower())
			decl = decl.upper()
		decrypt = decrypt + decl
	return decrypt

def mappingCypher():
	opt = raw_input('MAP: Please input a option (ENC,DEC):)')
	txt = raw_input('MAP: Please input the text          :)')
	if opt == 'ENC':
		print encryptMapping(txt)
	elif opt == 'DEC':
		print decryptMapping(txt)
