# scc is shortcut for Simple cipher code.
def finder(d,value):
    for k, v in d.items():
        if v == value: return k
    return -1
        

# dont use handle now:::
def handle(inputs,howto):
    holding = []
    mapping = {}
    translist = []
    inputinbin = []
    new_text = ''
    doit = 'unknown'
    howto = howto.split(' ')
    if howto[0] == 'enc' or 'dec':
        doit = howto[0]
    else:
        return 'Fail!!!!!!'

    # to howto[1]
    if howto[1] == 'intobin':
        for i in inputs:
            inputinbin.append(bin(ord(i))[2:])
        #print inputinbin
    # mapping
    elif howto[1][0] == '<' and howto[1][len(howto[1])-1] == '>':
        holding = howto[1][1:-1].split(',')
        for i in holding:
            v = i.split(':')
            mapping[v[0]] = v[1]
        for i in inputs:
            if doit == 'enc':
                new_text += mapping[i]
            elif doit == 'dec':
                new_text += finder(mapping,i)
    # transposition
    elif howto[1][0] == '[' and howto[1][len(howto[1])-1] == ']':
        holding = howto[1][1:-1].split(',')
        translist = holding
        if doit == 'enc':
            for i in translist:
                new_text += inputs[int(i)]
    return new_text


'''
inputs = input('INPUT ...')
howto = input('PLEASE ENTER THE WAY ...')

print(handle(inputs,howto))
'''

def mapping(inputs,key,howto):
    new_text = ''
    for i in inputs:
        if howto == 'enc':
            new_text += key[i]
        elif howto == 'dec':
            new_text += finder(key,i)
    return new_text

print(mapping('abc',{'a':'b','b':'c','c':'a'},'enc'))
print(mapping('bca',{'a':'b','b':'c','c':'a'},'dec'))