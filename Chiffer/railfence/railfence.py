def genrangelist(key, length):
	rangelist1 = range(0,key)
	rangelist2 = range(key-2,0,-1)
	rangelist = rangelist1 + rangelist2
	num = length/len(rangelist)
	rem = length%len(rangelist)
	longrangelist = rangelist*num + rangelist[:rem]
	return longrangelist

def encrypt(plain,key,rangelist):
	enclist = list()
	enctext = ''
	for i in range(key):
		enclist.append('')
	for i in range(0,len(plain)):
		enclist[rangelist[i]] = enclist[rangelist[i]] + plain[i]
	for i in range(len(enclist)):
		enctext = enctext + enclist[i]
	return enctext
	
def findx(x,rangelist):
	find = 0
	for i in rangelist:
		if i == x:
			find = find + 1
	return find
	
def genrail(encrypttext,key,rangelist):
	raillist = list()
	start = 0
	for i in range(key):
		length = findx(i,rangelist)
		end = start + length
		raillist.append(encrypttext[start:end])
		start = end
	return raillist

def decrypt(key,rangelist,rail):
	msg = ''
	next = list()
	for i in range(key):
		next.append(0)
	for i in rangelist:
		msg = msg + rail[i][next[i]]
		next[i] = next[i] + 1
	return msg
	
strKey = raw_input('please input a key ->')	
key = int(strKey)
plain = str(raw_input('please input a plaintext ->'))
print encrypt(plain,key,genrangelist(key, len(plain)))
encrypttext = str(raw_input('please input a encrypttext ->'))
print decrypt(key,genrangelist(key, len(plain)),genrail(encrypttext,key,genrangelist(key, len(plain))))