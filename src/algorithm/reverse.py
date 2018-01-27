from .base_transposition import base_transposition

class reverse(base_transposition):
    def encList(self, text):
        return list(range(len(text)-1,-1,-1))