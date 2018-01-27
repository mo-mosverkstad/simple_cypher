from .base_mapping import base_mapping

class shuffle(base_mapping):
    def encList(self):
        new_list = list()
        for i in range(0, len(self.whole_list),int(self.key)):
            new_list += list(reversed(self.whole_list[i:i+int(self.key)]))
        return new_list