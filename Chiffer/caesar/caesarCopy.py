letters_low = 'abcdefghijklmnopqrstuvwxyz'
letters_up  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_num = '0123456789'

def letter(plaintextl,letters,key):
	if plaintextl in letters:
		plindex  = letters.find(str(plaintextl))
		encindex = plindex + key
		if encindex >= len(letters):
			encindex = encindex - len(letters)
		elif encindex < 0:
			encindex = encindex + len(letters)
		return letters[encindex]
	else:
		return plaintextl
		
def caesar(plaintext,key):
	msg = ''
	for letters in plaintext:
		if letters in letters_low:
			ce = letter(letters,letters_low,key)
		elif letters in letters_up:
			ce = letter(letters,letters_up,key)
		elif letters in letters_num:
			ce = letter(letters,letters_num,key)
		else:
			ce = letters
		msg = msg + ce
	return msg

plakey      = int(raw_input('please input a key:'))
plaintext  	= str(raw_input('please input a plaintext: '))
print caesar(plaintext,plakey)
enckey      = int(raw_input('please input a key: '))
encrypttext = str(raw_input('please input a encrypttext: '))
print caesar(encrypttext,enckey)