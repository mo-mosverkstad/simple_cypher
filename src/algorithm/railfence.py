import operator
from .base_transposition import base_transposition

class railfence(base_transposition):
    def __init__(self, howto, key):
        super().__init__(howto, key)
        self.key = int(key)

    def plainList(self, text):
        text_len = len(text)
        l = (list(range(self.key))+list(range(self.key-2,0,-1)))
        repeat = int(text_len/(2*self.key-2))
        rem = text_len%(2*self.key-2)
        long_list = l*repeat + l[:rem]
        railfence_dict = dict(zip(list(range(text_len)), long_list))
        sorteds = sorted(railfence_dict.items(), key=operator.itemgetter(1))
        return [i[0] for i in sorteds]


        
