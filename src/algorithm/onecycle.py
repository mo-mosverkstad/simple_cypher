from .base_transposition import base_transposition

class onecycle(base_transposition):
    def __init__(self, howto, key):
        super().__init__(howto, key)
        self.key = int(key)

    def plainList(self, text):
        l = []
        for i in range(self.key-1,len(text),self.key):
            l.append(i)
        return l
    
    def encList(self,text):
        l = self.plainList(text)
        l = l[1:] + l[:1]
        return l