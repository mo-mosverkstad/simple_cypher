alphabet = 'abcdefghijklmnopqrstuvwxyz'

def gencipher():
	cipher = ''
	for index in range(25,-1,-1):
		cipher = cipher + alphabet[index]
	return cipher

def atbletter(pl,cipher):
	index = alphabet.index(str(pl))
	encryptletter = cipher[index]
	return encryptletter
	
def atb(p,c):
	msg = ''
	for letter in p:
		if letter in alphabet:
			enctext = atbletter(letter,c)
			msg = msg + enctext
		else:
			msg = msg + letter
	return msg

plaintext = raw_input('please input text ->')
print atb(plaintext,gencipher())