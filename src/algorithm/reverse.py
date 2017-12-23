from .base_transposition import base_transposition

class reverse(base_transposition):
    def cypher(self, text):
        return ''.join(list(reversed(text)))