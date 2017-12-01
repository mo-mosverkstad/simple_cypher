alphabet = 'abcdefghijklmnopqrstuvwxyz'

def genVTabell():
	vtabell = [alphabet]
	for i in range(1,26):
		vtabell.append(alphabet[i:26] + alphabet[0:i])
	return vtabell

def genLongKey(l, key):
	length=len(key)
	return key*(l/length) + key[0:(l%length)]

def vigEncrypt(vtabell, plain, longKey):
	encText = ''
	for i in range(0,len(plain)):
		if plain[i] in alphabet:
			hotell = alphabet.find(str(longKey[i]))
			room = alphabet.find(str(plain[i]))
			encText = encText + vtabell[hotell][room]
		else:
			encText = encText + plain[i]
	return encText

def vigDecrypt(vtabell, encrypt, longKey):
	plainText = ''
	for i in range(0,len(encrypt)):
		if encrypt[i] in alphabet:
			hotell = alphabet.find(str(longKey[i]))
			room = vtabell[hotell].find(encrypt[i])
			plainText=plainText+alphabet[room]
		else:
			plainText=plainText+encrypt[i]
	return plainText
	

v = genVTabell()
opt   = str(raw_input('please input an option->'))
key   = str(raw_input('please input a key->'))

if opt == 'ENC':
	plain = str(raw_input('please input a text->'))
	longKey = genLongKey(len(plain), key)
	encrypt = vigEncrypt(v, plain, longKey)
	print encrypt
elif opt == 'DEC':
	encrypt = str(raw_input('please input a cypher->'))
	longKey = genLongKey(len(encrypt), key)
	plain = vigDecrypt(v, encrypt, longKey)
	print plain




