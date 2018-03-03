class base_transposition:
    def __init__(self, howto, key):
        self.howto = howto
        self.key = int(key)
        self.type = 'TRANSPOSITION'

    def plainList(self,text):#this i will change
        return list(range(len(text)))

    def encList(self,text):# this i will change
        return list(range(len(text)))

    def transposition_core(self,d,txt):
        new_txt_list = [' ']*len(txt)
        for i in range(0, len(txt)):
            new_txt_list[d.get(i,i)] = txt[i]
        return ''.join(new_txt_list)

    def enc_key(self,text):
        return dict(zip(self.plainList(text),self.encList(text)))

    def dec_key(self,text):
        return dict(zip(self.encList(text),self.plainList(text)))

    def __inner_cypher(self, text):
        if self.howto == 'enc':
            d = self.enc_key(text)
        else:
            d = self.dec_key(text)
        return self.transposition_core(d,text)

    def cypher(self,text):
        return self.__inner_cypher(text)