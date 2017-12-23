# ========================= CODING FILE INFORMATION ========================= #
# File         : core.py
# Date         : 2017-Dec-23
# Last modified: 2017-Dec-23
#
# Author       : Mo
#
# Description  : This core.py handle encryption and decryption
#
# Dependency   : Python 3.6
#
# Usage        : -
# =========================================================================== #

# handle_cypher(text, codec_dict) -> encrypted or decrypted text

def handle_cypher(text, codec_dict):
    new_text = str()
    for c in text:
        new_text += codec_dict[c]
    return new_text
    #return ''.join([codec_dict[c] for c in plain])
