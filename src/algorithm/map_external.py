from .base_mapping import base_mapping

class map_external(base_mapping):
    def __enc_dict(self):
        return dict(zip(self.whole_list, eval(self.key)))

    def __dec_dict(self):
        return dict(zip(eval(self.key), self.whole_list))

    def cypher(self, text):
        return super().cypher(text, self.__enc_dict(), self.__dec_dict())