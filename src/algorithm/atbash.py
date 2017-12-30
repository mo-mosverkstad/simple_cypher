from .base_mapping import base_mapping

class atbash(base_mapping):
    def __enc_dict(self):
        return dict(zip(self.whole_list,''.join(list(reversed(self.whole_list)))))

    def __dec_dict(self):
        return dict(zip(''.join(list(reversed(self.whole_list))),self.whole_list))

    def cypher(self, text):
        return super().cypher(text, self.__enc_dict(), self.__dec_dict())