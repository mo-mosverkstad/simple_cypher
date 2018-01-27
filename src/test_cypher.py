from profile import handle_profile
from core import handle_cypher

test_data_dict = {'TC_CAESAR_ENC_+3': ('abcdefg',  'enc#caesar#+3', 'defghij'),  \
                  'TC_CAESAR_DEC_+3': ('defghij',  'dec#caesar#+3', 'abcdefg'),  \
                  'TC_SHUFFLE_ENC_4': ('abcdefgh', 'enc#shuffle#4', 'dcbahgfe'), \
                  'TC_SHUFFLE_DEC_4': ('dcbahgfe', 'dec#shuffle#4', 'abcdefgh'), \
                  'TC_REVERSE_ENC':   ('ADEBGKOT', 'enc#reverse#',  'TOKGBEDA'), \
                  'TC_REVERSE_DEC':   ('TOKGBEDA', 'dec#reverse#',  'ADEBGKOT'), \
                  'TC_ONECYCLE_ENC_2':('O5QR37N9', 'enc#onecycle#2','O9Q53RN7'), \
                  'TC_ONECYCLE_DEC_2':('O9Q53RN7', 'dec#onecycle#2','O5QR37N9'), \
                  'TC_RAILFENCE_ENC3':('PLAINTXT', 'enc#railfence#3','PNLITTAX'), \
                  'TC_RAILFENCE_DEC3':('PNLITTAX', 'dec#railfence#3','PLAINTXT'), \
                  'TC_ATBASH_ENC____':('ABCDEF', 'enc#atbash#' , 'JIHGFE'), \
                  'TC_ATBASH_DEC____':('JIHGFE', 'dec#atbash#' , 'ABCDEF')}

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