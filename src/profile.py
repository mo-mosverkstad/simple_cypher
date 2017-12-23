# ========================= CODING FILE INFORMATION ========================= #
# File         : profile.py
# Date         : 2017-Dec-22
# Last modified: 2017-Dec-23
#
# Author       : Mo
#
# Description  : This profile.py file provides the codec dictionary by profile
#
# Dependency   : Python 3.6, re
#
# Usage        : -
# =========================================================================== #

# handle_profile(profile) -> codec_dict
# profile = <howto: enc/dec>#<algorithm>#<key>

import re

def generate_ascii_list(start, stop):
    return [chr(c) for c in range(start, stop)]

def lowcase_list():
    return generate_ascii_list(97, 123)

def upcase_list():
    return generate_ascii_list(65, 91)

def digit_list():
    return generate_ascii_list(48, 58)

def caesar_enc(key):
    k = int(key)
    whole_list = lowcase_list() + upcase_list() + digit_list()
    return dict(zip(whole_list, whole_list[k:]+whole_list[:k]))

def caesar_dec(key):
    k = int(key)
    whole_list = lowcase_list() + upcase_list() + digit_list()
    return dict(zip(whole_list[k:]+whole_list[:k], whole_list))

def handle_profile(profile):
    howto, algorithm, key = re.split('#', profile)
    func_str = algorithm + '_' + howto
    return eval(func_str)(key)
