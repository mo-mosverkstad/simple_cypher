# ========================= CODING FILE INFORMATION ========================= #
# File         : wrapper.py
# Date         : 2017-Dec-23
# Last modified: 2017-Dec-23
#
# Author       : Mo
#
# Description  : The cli wrapper for scc (Simple Cypher Coding)
#
# Dependency   : Python 3.6, re
#
# Usage        : python wrapper.py
# =========================================================================== #

# cli input:
#     - text, which could be plain text for encryption or encrypted text for decryption.
#     - profile, the format: <howto: enc/dec>#<algorithm>#<key>

import re

def wrapper(text,key):
    continueflag = True
    sub_keys = key.split('#')
    if len(sub_keys) == 3:
        continueflag = True
    else:
        continueflag = False
