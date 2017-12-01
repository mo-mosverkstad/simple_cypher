upcase  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def findIndex(array, key):
    index = -1
    for i in range(0, len(array)):
        if array[i] == key:
            index = i
            break
    return index

i = findIndex(lowcase, raw_input('input a lowcase letter: '))
if i == -1: print "wrong input!"
else:
    i = i + 5
    if i > 25: i = i - 26
    print lowcase[i]