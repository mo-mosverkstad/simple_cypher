# ========================= CODING FILE INFORMATION ========================= #
# File         : prof_mgmt.py
# Date         : 2018-Jan-04
# Last modified: 2018-Feb-02
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

from data_mgmt import data_read_prof, data_write_prof, algorithm_write_in, algorithm_remove

CODE_BUILT_IN = '<built in>'

def find_type(prof_dict, algorithm):
    for keys, contents in list(prof_dict.items()):
        for k,v in list(contents.items()):
            if k == algorithm:
                return keys
    return None

def prof_list ():
    #return(data_read_prof())
    display_list = str()
    for algorithm_type, algorithms in data_read_prof().items():
        display_list += '%s\n'%(algorithm_type)
        for algorithm, code in algorithms.items():
            display_list += '\t%s\t%s\n'%(algorithm, code)
    return display_list

def prof_new (type, algorithm):
    prof_dict = data_read_prof()
    prof_dict[type][algorithm] = ''
    data_write_prof(prof_dict)

def prof_edit (algorithm, fcode,scode, descryption):
    prof_dict = data_read_prof()
    algorithm_type = find_type(prof_dict, algorithm)
    if algorithm_type != None and prof_dict[algorithm_type][algorithm] != CODE_BUILT_IN:
        prof_dict[algorithm_type][algorithm] = descryption
    data_write_prof(prof_dict)
    algorithm_write_in(algorithm_type,algorithm,fcode,scode)

def prof_delete (algorithm):
    prof_dict = data_read_prof()
    algorithm_type = find_type(prof_dict, algorithm)
    if algorithm_type != None and prof_dict[algorithm_type][algorithm] != CODE_BUILT_IN:
        del prof_dict[algorithm_type][algorithm]
    data_write_prof(prof_dict)
    algorithm_remove(algorithm)



