# key defination(constants defination):

key1 = int(raw_input('key1:'))### number of rows
key2 = raw_input('key2:')     ### starting position
key3 = 'clockwise'            ### direction

# constants defination before functions defination:

#plaintext = 'we are discovered flee at once'
plaintext = raw_input('please input a plaintext :>')

# functions defination:

def reverse(plainText):
	chiffer = ''
	for i in range(len(plainText)-1,-1,-1):
		chiffer = chiffer + plainText[i]
	return chiffer

def gentext(key,plaintext):
    addn = len(plaintext) % key
    if addn != 0:
         plaintext = plaintext + ' '*(key - addn)
    array = []
    for i in range(len(plaintext)/key):
        for j in range(key):
            array.append(j)
    newlist = []
    for i in range(key):
        newlist.append('')
    for i in range(len(plaintext)):
        newlist[array[i]] = newlist[array[i]] + plaintext[i]
    return newlist

def encrypt(key1,key2,key3,plaintext):
    plain = gentext(key1,plaintext)
    msg = ''
    while plain != []:
        count = 0
        for i in plain:
            if i != '':
                count = count + 1
        if count == 0:
            return msg
        enc1 = ''
        enc2 = ''
        enc3 = ''
        enc4 = ''
        enc1 = plain[0][0:len(plain[0])-1]
        #print 'plain: ', plain
        #print '"' + enc1 + '"' + 'length:' + str(len(enc1))
        for i in range(key1-1):
            #print 'i:', i
            enc2 = enc2 + plain[i][len(plain[i])-1]
        #print '"' + enc2 + '"'+ 'length:' + str(len(enc2))
        enc3 = reverse(plain[key1-1][1:])
        #print '"' + enc3 + '"'+ 'length:' + str(len(enc3))
        for i in range(key1-1,0,-1):
            enc4 = enc4 + plain[i][0]
        #print '"' + enc4 + '"'+ 'length:' + str(len(enc4))
        if key3 == 'clockwise':
            if key2 == 'top left':
                msg = msg + enc1+enc2+enc3+enc4 
            elif key2 == 'top right':
                msg = msg + enc2+enc3+enc4+enc1
            elif key2 == 'bottom right':
                msg = msg + enc3+enc4+enc1+enc2
            elif key2 == 'bottom left':
                msg = msg + enc4+enc1+enc2+enc3
        plain = plain[1:len(plain)-1]
        if plain == []:
            return msg
        else:
            for i in range(len(plain)):
                plain[i] = plain[i][1:len(plain[i])-1]
        key1 = key1 - 2
    return msg
        

# begin:
print encrypt(key1,key2,key3,plaintext)
