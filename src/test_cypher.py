from profile import handle_profile
from core import handle_cypher

test_data_dict = {'TC_CAESAR_ENC_+3': ('abcdefg', 'enc#caesar#+3', 'defghij'), \
                  'TC_CAESAR_DEC_+3': ('defghij', 'dec#caesar#+3', 'abcdefg'), \
                  'TC_SHUFFLE_ENC_4': ('abcdefgh', 'enc#shuffle#4', 'dcbahgfe'), \
                  'TC_SHUFFLE_DEC_4': ('dcbahgfe', 'dec#shuffle#4', 'abcdefgh')}

def run_test(test_data_value):
    text, profile, expect = test_data_value
    return handle_cypher(text, handle_profile(profile))==expect

def run_tests(test_data_dict):
    pass_number = 0
    for k, v in test_data_dict.items():
        if run_test(v): pass_number += 1
        else: print(f'{k}: error!!!')
    total_number = len(test_data_dict)
    print(f'Pass rate: {pass_number/total_number*100}%, ({pass_number} out of {total_number})')

run_tests(test_data_dict)