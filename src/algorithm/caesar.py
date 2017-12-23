from .base_mapping import base_mapping

class caesar(base_mapping):
    def __enc_dict(self):
        return dict(zip(self.whole_list, self.whole_list[self.key:] + self.whole_list[:self.key]))

    def __dec_dict(self):
        return dict(zip(self.whole_list[self.key:] + self.whole_list[:self.key], self.whole_list))

    def cypher(self, text):
        return base_mapping.cypher(self, text, self.__enc_dict(), self.__dec_dict())