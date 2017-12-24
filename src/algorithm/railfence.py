import operator
from .base_transposition import base_transposition

class railfence(base_transposition):
    def __init__(self, howto, key):
        super().__init__(howto, key)
        self.key = int(key)

    def __generate_railfence_list(self, text_len):
        l = (list(range(self.key))+list(range(self.key-2,0,-1)))
        repeat = int(text_len/(2*self.key-2))
        rem = text_len%(2*self.key-2)
        long_list = l*repeat + l[:rem]
        railfence_dict = dict(zip(list(range(text_len)), long_list))
        sorteds = sorted(railfence_dict.items(), key=operator.itemgetter(1))
        return [i[0] for i in sorteds]

    def __generate_railfence_dict(self, list_1, list_2):
        return dict(zip(list_1, list_2))

    def __enc_railfence(self,text):
        return self.transposition_core( \
            self.__generate_railfence_dict(self.__generate_railfence_list(len(text)), list(range(len(text)))), \
            text)

    def __dec_railfence(self,text):
        return self.transposition_core( \
            self.__generate_railfence_dict(list(range(len(text))),self.__generate_railfence_list(len(text))), \
            text)


    def cypher(self, text):
        if self.howto == 'enc': return self.__enc_railfence(text)
        else: return self.__dec_railfence(text)
        
