from .base_mapping import base_mapping

class caesar(base_mapping):
    def encList(self):
        return self.whole_list[int(self.key):] + self.whole_list[:int(self.key)]