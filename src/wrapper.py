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
PROMPT_PROF   = 'PROF:>>'

COMMAND_EXIT = 'exit'
COMMAND_PROFILE = 'prof'
COMMAND_UP = 'up'
COMMAND_ENC = 'enc '
COMMAND_DEC = 'dec '
COMMAND_EDIT = 'edit'

CONFIG_HOWTO = 'enc'
CONFIG_ALGORITHM = 'caesar'
CONFIG_KEY = '+3'

def system_exit(current_status, algorithm, key):
    sys.exit()
    return current_status, algorithm, key


def system_profile(current_status, algorithm, key):
    return PROMPT_PROF, algorithm, key

def system_up(current_status, algorithm, key):
    return PROMPT_ROOT, algorithm, key

def system_config_edit(current_status, algorithm, key):
    print(f'The current algorithm is "{algorithm}"')
    print(f'The current key is "{key}"')
    algorithm = input('algorithm...')
    key       = input('key      ...')
    print('Algorithm "%s" and key "%s" are changed now.'%(algorithm, key))
    return PROMPT_ROOT, algorithm, key

SCC_DICT = {PROMPT_ROOT:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_PROFILE: 'system_profile',
                 COMMAND_EDIT: 'system_config_edit'},
            PROMPT_PROF:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_UP: 'system_up'},
           }

def get_scc_dict_values():
    return [func for cmd in SCC_DICT.values() for func in cmd.values()]

def wrapper(howto=CONFIG_HOWTO, algorithm=CONFIG_ALGORITHM, key=CONFIG_KEY):
    status = PROMPT_ROOT
    while True:
        command = input(status)
        func_str = SCC_DICT[status].get(command)
        if func_str in get_scc_dict_values():
            status, algorithm, key = eval(func_str + '(status, algorithm, key)')
        elif (command.startswith(COMMAND_ENC) or command.startswith(COMMAND_DEC)) and (status == PROMPT_ROOT):
            howto = command[:3]
            text = command[4:]
            prof = howto + '#' + algorithm + '#' + key
            print(handle_cypher(text, handle_profile(prof)))
            


wrapper()