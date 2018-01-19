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
from prof_mgmt import prof_list, prof_new, prof_edit, prof_delete

PROMPT_ROOT   = 'SCC:>'
PROMPT_PROF   = 'PROF:>>'
PROMPT_EXIT   = 'EXIT'

COMMAND_EXIT = 'exit'
COMMAND_PROFILE = 'prof'
COMMAND_UP = 'up'
COMMAND_ENC = 'enc '
COMMAND_DEC = 'dec '
COMMAND_EDIT = 'edit'
COMMAND_LIST = 'list'
COMMAND_NEW = 'new'
COMMAND_DELETE = 'delete'

CONFIG_HOWTO = 'enc'
CONFIG_ALGORITHM = 'caesar'
CONFIG_KEY = '+3'

def system_exit(current_status, algorithm, key):
    return PROMPT_EXIT, algorithm, key


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

def system_prof_list(current_status, algorithm, key):
    print(prof_list())
    return current_status, algorithm, key

def system_prof_new(current_status, algorithm, key):
    algorithm_type = input('Please input algorithm type:')
    algorithm_name = input('Please input algorithm name:')
    prof_new(algorithm_type, algorithm_name)
    return current_status, algorithm, key

def system_prof_edit(current_status, algorithm, key):
    print('Warning! Your old will be changed if you enter in edit mode.')
    check = input('Are you sure that you want go into edit mode? Answer yes or no:')
    if check == 'yes':
        algorithm_name = input('Please input algorithm name(in edit mode):')
        code           = input('Please input your new code here          :')
        prof_edit(algorithm_name,code)
    return current_status, algorithm, key

def system_prof_del(current_status, algorithm, key):
    print('Warning! Your profile will be deleted')
    check = input('Are you sure you want delete this profile? If you want this profile will be deleted forever!! Answer yes or no:')
    if check == 'yes':
        algorithm_name = input('Please enter profile name:')
        new_check = input(f'Are you sure you want to delete {algorithm_name}? Your profile {algorithm_name} will be deleted forever! Answer yes or no:')
        if new_check == 'yes':
            prof_delete(algorithm_name)
    return current_status, algorithm, key

SCC_DICT = {PROMPT_ROOT:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_PROFILE: 'system_profile',
                 COMMAND_EDIT: 'system_config_edit'},
            PROMPT_PROF:
                {COMMAND_EXIT: 'system_exit',
                 COMMAND_LIST: 'system_prof_list',
                 COMMAND_NEW:  'system_prof_new',
                 COMMAND_EDIT: 'system_prof_edit',
                 COMMAND_DELETE:'system_prof_del',
                 COMMAND_UP: 'system_up'},
           }

def get_scc_dict_values():
    return [func for cmd in SCC_DICT.values() for func in cmd.values()]

def scc_wrapper(howto=CONFIG_HOWTO, algorithm=CONFIG_ALGORITHM, key=CONFIG_KEY):
    status = PROMPT_ROOT
    while True:
        command = input(status)
        func_str = SCC_DICT[status].get(command)
        if func_str in get_scc_dict_values():
            status, algorithm, key = eval(func_str + '(status, algorithm, key)')
            if status == PROMPT_EXIT:
                break
        elif (command.startswith(COMMAND_ENC) or command.startswith(COMMAND_DEC)) and (status == PROMPT_ROOT):
            howto = command[:3]
            text = command[4:]
            prof = howto + '#' + algorithm + '#' + key
            print(handle_cypher(text, handle_profile(prof)))


scc_wrapper()