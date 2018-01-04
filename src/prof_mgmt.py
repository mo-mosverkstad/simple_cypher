# ========================= CODING FILE INFORMATION ========================= #
# File         : prof_mgmt.py
# Date         : 2018-Jan-04
# Last modified: 2018-Jan-04
#
# Author       : Mo
#
# Description  : This file is used for profile management
#
# Dependency   : Python 3.6
#
# Usage        : -
# =========================================================================== #

# prof_list () -> dictionary of all of profiles, {mapping: [caesar, atbash,...], 
#                                                 transposition: [...]}
# prof_new  (type, algorithm) -> None
# prof_edit (algorithm, code) -> None
# prof_delete (algorithm) -> None

CODE_BUILT_IN = '<built in>'

prof_dict = {'mapping':{'atbash':CODE_BUILT_IN,
                        'caesar':CODE_BUILT_IN,
                        'shuffle':CODE_BUILT_IN},
             'transposition':{'onecycle':CODE_BUILT_IN,
                              'railfence':CODE_BUILT_IN,
                              'reverse':CODE_BUILT_IN}
             }

def find_type(algorithm):
    for keys, contents in list(prof_dict.items()):
        for k,v in list(contents.items()):
            if k == algorithm:
                return keys
    return None

def prof_list ():
    return prof_dict

def prof_new (type, algorithm):
    prof_dict[type][algorithm] = ''

def prof_edit (algorithm, code):
    type = find_type(algorithm)
    if type != None and prof_dict[type][algorithm] != CODE_BUILT_IN:
        prof_dict[find_type(algorithm)][algorithm] = code

def prof_delete (algorithm):
    type = find_type(algorithm)
    if type != None and prof_dict[type][algorithm] != CODE_BUILT_IN:
        del prof_dict[find_type(algorithm)][algorithm]

