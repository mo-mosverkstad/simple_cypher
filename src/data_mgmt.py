# ========================= CODING FILE INFORMATION ========================= #
# File         : prof_mgmt.py
# Date         : 2018-Jan-07
# Last modified: 2018-Jan-07
#
# Author       : Mo
#
# Description  : This file is used for data management
#
# Dependency   : Python 3.6
#
# Usage        : -
# =========================================================================== #

# data_read_prof () -> the dictionary of prof
# data_write_prof(prof_dict) -> None

data_prof_file = 'scc_prof.data'
data_delimitor = ';'

def data_read_prof():
    prof_dict = dict()
    with open(data_prof_file, 'r') as f:
        for line in f.readlines():
            if data_delimitor in line:
                algorithm_type, algorithm, code = line.rstrip().split(data_delimitor)
                if not algorithm_type in prof_dict:
                    prof_dict[algorithm_type] = dict()
                prof_dict[algorithm_type][algorithm] = code
    return prof_dict

def data_write_prof(prof_dict):
    with open(data_prof_file, 'w') as f:
        for algorithm_type, contents in prof_dict.items():
            for algorithm, code in contents.items():
                f.write(algorithm_type + data_delimitor + algorithm + data_delimitor + code + '\n')