from .base_mapping import base_mapping

class atbash(base_mapping):
    def encList(self):
        return ''.join(list(reversed(self.whole_list)))