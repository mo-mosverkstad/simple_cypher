class base_mapping:
    def __init__(self, howto, key):
        self.howto = howto
        self.key = int(key)
        self.whole_list = self.__lowcase_list() + self.__upcase_list() + self.__digit_list()
        self.type = 'MAPPING'

    def __generate_ascii_list(self, start, stop):
        return [chr(c) for c in range(start, stop)]

    def __lowcase_list(self):
        return self.__generate_ascii_list(97, 123)

    def __upcase_list(self):
        return self.__generate_ascii_list(65, 91)

    def __digit_list(self):
        return self.__generate_ascii_list(48, 58)

    def cypher(self, text, enc_dict, dec_dict):
        codec_dict = enc_dict if self.howto == 'enc' else dec_dict
        return ''.join([codec_dict[c] for c in text])