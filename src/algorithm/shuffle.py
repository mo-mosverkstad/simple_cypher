from .base_mapping import base_mapping

class shuffle(base_mapping):
    def __enc_dec_dict(self):
        enc_dict = {}
        for i in range(0, len(self.whole_list),int(self.key)):
            place = self.whole_list[i:i+int(self.key)]
            newplace = list(reversed(place))
            enc_dict.update(dict(zip(place,newplace)))
        return enc_dict

    def cypher(self, text):
        return base_mapping.cypher(self, text, self.__enc_dec_dict(), self.__enc_dec_dict())