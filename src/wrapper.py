# ========================= CODING FILE INFORMATION ========================= #
# File         : wrapper.py
# Date         : 2017-Dec-23
# Last modified: 2017-Dec-30
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
from profile import handle_profile
from core import handle_cypher

PROMPT = ' >>>'
PROMPT_TEXT = 'TEXT' + PROMPT
PROMPT_PROF = 'PROF' + PROMPT


def wrapper():
    exitFlag = False
    while not exitFlag:
        text = input(PROMPT_TEXT)
        prof = input(PROMPT_PROF)
        if text == 'exit' and prof == '':
            exitFlag = True
        print(handle_cypher(text, handle_profile(prof)))

wrapper()