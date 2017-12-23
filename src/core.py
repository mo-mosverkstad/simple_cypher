# ========================= CODING FILE INFORMATION ========================= #
# File         : core.py
# Date         : 2017-Dec-23
# Last modified: 2017-Dec-23
#
# Author       : Mo
#
# Description  : This core.py handle encryption and decryption
#
# Dependency   : Python 3.6
#
# Usage        : -
# =========================================================================== #

# handle_cypher(text, algorithm_obj) -> encrypted or decrypted text

def handle_cypher(text, algorithm_obj):
    return algorithm_obj.cypher(text)