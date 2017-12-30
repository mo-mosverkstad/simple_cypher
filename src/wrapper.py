# ========================= CODING FILE INFORMATION ========================= #
# File         : wrapper.py
# Date         : 2017-Dec-23
# Last modified: 2017-Dec-30
#
# Author       : Mo
#
# Description  : The cli wrapper for scc (Simple Cypher Coding)
#
# Dependency   : Python 3.6, re, sys
#
# Usage        : python wrapper.py
# =========================================================================== #

# cli input:
#     - text, which could be plain text for encryption or encrypted text for decryption.
#     - profile, the format: <howto: enc/dec>#<algorithm>#<key>

import re
import sys
from profile import handle_profile
from core import handle_cypher

PROMPT_ROOT   = 'SCC:>'
PROMPT_CYPHER = 'CYPHER:>>'
PROMPT_PROF   = 'PROF:>>'

COMMAND_EXIT = 'exit'
COMMAND_CYPHER = 'cypher'
COMMAND_PROFILE = 'prof'
COMMAND_UP = 'up'

def system_exit(current_status):
    sys.exit()
    return current_status

def system_cypher(current_status):
    return PROMPT_CYPHER

def system_profile(current_status):
    return PROMPT_PROF

def system_up(current_status):
    return PROMPT_ROOT

SCC_DICT = {PROMPT_ROOT:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_CYPHER: 'system_cypher',
                 COMMAND_PROFILE: 'system_profile'},
            PROMPT_CYPHER:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_UP: 'system_up'},
            PROMPT_PROF:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_UP: 'system_up'}}

def wrapper():
    status = PROMPT_ROOT
    while True:
        command = input(status)
        #print(SCC_DICT[status][command] + '(status)')
        func_str = SCC_DICT[status].get(command)
        if func_str != None:
            status = eval(func_str + '(status)')

wrapper()