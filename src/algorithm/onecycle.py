from .base_transposition import base_transposition

class onecycle(base_transposition):
    def __init__(self, howto, key):
        super().__init__(howto, key)
        self.key = int(key)

    def __enc_onecycle(self, text):
        l = []
        for i in range(self.key-1,len(text),self.key):
            l.append(i)
        newl = l[1:] + l[:1]
        d = dict(zip(l,newl))
        return self.transposition_core(d,text)
    
    def __dec_onecycle(self,text):
        l = []
        for i in range(self.key-1,len(text),self.key):
            l.append(i)
        newl = l[1:] + l[:1]
        d = dict(zip(newl,l))
        return self.transposition_core(d,text)

    def cypher(self, text):
        if self.howto == 'enc': return self.__enc_onecycle(text)
        else: return self.__dec_onecycle(text)