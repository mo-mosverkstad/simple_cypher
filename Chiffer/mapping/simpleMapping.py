plain  = 'abcdefghijklmnopqrstuvwxyz'
cypher = 'dcbahgfelkjiponmtsrqxwvuzy'

#plainText = 'a boy is named after remus'
#decryptText = 'd cnz lr odpha dgqhs shpxr'

def encryptMappingLetter(p):
	if p in plain:
		encryptindex = plain.find(p)
		enc = cypher[encryptindex]
		return enc
	else:
		return p
	
def encryptMapping(plainText):
	msg = ''
	for i in plainText:
		enc = encryptMappingLetter(i)
		msg = msg + enc
	return msg


def decryptMappingLetter(e):
	if e in plain:
		decryptindex = cypher.find(e)
		dec = plain[decryptindex]
		return dec
	else:
		return e

def decryptMapping(encryptText):
	msg = ''
	for i in encryptText:
		dec = decryptMappingLetter(i)
		msg = msg + dec
	return msg
		
		
#print decryptMapping(decryptText)	
#print encryptMapping(plainText)