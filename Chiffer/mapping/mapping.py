alphabet = 'abcdefghijklmnopqrstuvwxyz'
mapping = [5, 21, 14, 23, 0, 11, 18, 9, 2, 4, 7, 15, 25, 16, 1, 8, 12, 20, 3, 6, 10, 13, 17, 19, 22, 24]


def encryptletter(l):
	i = alphabet.index(l)
	encIndex = mapping[i]
	return alphabet[encIndex]

def encryptMapping(s):
	encrypt = ''
	for l in s:
		if l in alphabet:
			encl = encryptletter(l)
			encrypt = encrypt + encl
		else:
			encrypt = encrypt + l
	return encrypt

def decryptletter(l):
	i = alphabet.find(l)
	decIndex = mapping.index(i)
	return alphabet[decIndex]

def decryptMapping(s):
	decrypt = ''
	for l in s:
		if l in alphabet:
			decl = decryptletter(l)
			decrypt = decrypt + decl
		else:
			decrypt = decrypt + l
	return decrypt


plain = str(raw_input('Please input a plain text ->'))
print encryptMapping(plain)

encrypt = str(raw_input('Please input a encrypt text ->')) 
print decryptMapping(encrypt)