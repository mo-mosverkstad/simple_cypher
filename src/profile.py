# ========================= CODING FILE INFORMATION ========================= #
# File         : profile.py
# Date         : 2017-Dec-22
# Last modified: 2017-Dec-23
#
# Author       : Mo
#
# Description  : This profile.py file provides the algorithm object by profile
#
# Dependency   : Python 3.6, re, profile_list
#
# Usage        : -
# =========================================================================== #

# handle_profile(profile) -> algorithm class object
# profile = <howto: enc/dec>#<algorithm>#<key>

import re

def handle_profile(profile):
    howto, algorithm, key = re.split('#', profile)
    exec(f'from algorithm.{algorithm} import {algorithm}')
    return eval(algorithm + '(howto, key)')
