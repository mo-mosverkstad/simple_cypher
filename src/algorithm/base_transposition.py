class base_transposition:
    def __init__(self, howto, key):
        self.howto = howto
        self.key = key
        self.type = 'TRANSPOSITION'

    def transposition_core(self,d,txt):
        new_txt_list = [' ']*len(txt)
        for i in range(0, len(txt)):
            new_txt_list[d.get(i,i)] = txt[i]
        return ''.join(new_txt_list)

    def cypher(self, text):
        return text