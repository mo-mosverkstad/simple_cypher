letters_low = 'abcdefghijklmnopqrstuvwxyz'
letters_up  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_num = '0123456789'


def caesarEncryptLetter(letters, l, step):
	if l in letters:
		li=letters.find(l)
		encl=li+step
		if encl>=len(letters):
			encl=encl-len(letters)
		elif encl < 0:
			encl=encl+len(letters)
		return letters[encl]
	else:
		return l

def caesarEncrypt(msg, step):
	msgce=''
	for letter in msg:
		if letter in letters_low:
			ce = caesarEncryptLetter(letters_low, letter, step)
		elif letter in letters_up:
			ce = caesarEncryptLetter(letters_up, letter, step)
		elif letter in letters_num:
			ce = caesarEncryptLetter(letters_num, letter, step)
		else:
			ce = letter
		msgce=msgce+ce
	return msgce

def caeCypher():
	key = int(raw_input('CAE: Please input the integer key:) '))
	txt = str(raw_input('CAE: Please input the text       :) '))
	print caesarEncrypt(txt, key)