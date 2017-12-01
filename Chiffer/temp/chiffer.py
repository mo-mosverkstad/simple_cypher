letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

l=raw_input()
i=letters.index(l)
i=i+5
if i>25:
    i=i-26
print letters[i]