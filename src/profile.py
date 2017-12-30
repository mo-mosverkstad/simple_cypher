# ========================= CODING FILE INFORMATION ========================= #
# File         : profile.py
# Date         : 2017-Dec-22
# Last modified: 2017-Dec-30
#
# Author       : Mo
#
# Description  : This profile.py file provides the algorithm object by profile
#
# Dependency   : Python 3.6, re, profile_list
#
# Usage        : -
# =========================================================================== #

# handle_profile(profile) -> algorithm class object if ok else error info str
# profile = <howto: enc/dec>#<algorithm>#<key>

import re

PROF_DELIMITER = '#'

def handle_profile(profile):
    check, howto, algorithm, key = check_profile(profile)
    if check:
        exec(f'from algorithm.{algorithm} import {algorithm}')
        return eval(algorithm + '(howto, key)')
    else:
        return None

def check_profile(profile):
    if len(profile.split(PROF_DELIMITER)) == 3:
        howto, algorithm, key = re.split(PROF_DELIMITER, profile)
        return True, howto, algorithm, key
    else:
        return False, None, None, None