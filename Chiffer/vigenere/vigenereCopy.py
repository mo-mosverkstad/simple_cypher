alphabet = 'abcdefghijklmnopqrstuvwxyz'

def genvigtabell():
	tabell = list()
	tabell.append(alphabet)
	for i in range(1,26):
		tabell.append(alphabet[i:26]+alphabet[0:i])
	return tabell
	
def genviglongkey(plaintext,key):
	return key*(len(plaintext)/len(key))+key[0:len(plaintext)%len(key)]
	
def vigencrypt(tabell,longkey,plaintext):
	msg = ''
	for i in range(0,len(plaintext)):
		if plaintext[i] in alphabet:
			plaintextindex = alphabet.index(str(plaintext[i]))
			longkeyindex   = alphabet.index(str(longkey[i]))
			msg = msg + tabell[longkeyindex][plaintextindex]
		else:
			msg = msg + plaintext[i]
	return msg

def vigdecrypt(tabell,longkey,encrypttext):
	msg = ''
	for i in range(0,len(encrypttext)):
		if encrypttext[i] in alphabet:
			encrypttextindex = alphabet.index(str(encrypttext[i]))
			longkeyindex     = alphabet.index(str(longkey[i]))
			index = tabell[longkeyindex].index(str(encrypttext[i]))
			msg   = msg + alphabet[index]
		else:
			msg = msg + encrypttext[i]
	return msg
	

plaintext   = 'i will stay at home'
encrypttext = 'k kkvn gvka ov jzag'
key = 'clock'

print vigencrypt(genvigtabell(), genviglongkey(plaintext, key), plaintext)
print vigdecrypt(genvigtabell(), genviglongkey(encrypttext, key), encrypttext)