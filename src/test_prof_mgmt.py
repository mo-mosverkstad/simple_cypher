from prof_mgmt import *

def prof_test_01():
    prof_test = {'mapping':{'atbash':'<built in>',
                            'caesar':'<built in>',
                            'shuffle':'<built in>',
                            'test':''},
                 'transposition':{'onecycle':'<built in>',
                                  'railfence':'<built in>',
                                  'reverse':'<built in>'}
                 }
    prof_new('mapping', 'test')
    prof_edit('atbash', 'i want to do something...')
    return(prof_list()==prof_test)

def prof_test_02():
    prof_test = {'mapping':{'atbash':'<built in>',
                            'caesar':'<built in>',
                            'shuffle':'<built in>',
                            'test':'___________________________'},
                 'transposition':{'onecycle':'<built in>',
                                  'railfence':'<built in>',
                                  'reverse':'<built in>'}
                 }
    prof_edit('test', '___________________________')
    return(prof_list()==prof_test)

def prof_test_03():
    prof_test = {'mapping':{'atbash':'<built in>',
                            'caesar':'<built in>',
                            'shuffle':'<built in>'},
                 'transposition':{'onecycle':'<built in>',
                                  'railfence':'<built in>',
                                  'reverse':'<built in>'}
                 }
    prof_delete('caesar')
    prof_delete('test')
    return(prof_list()==prof_test)

def prof_test_04():
    prof_test = {'mapping':{'atbash':'<built in>',
                            'caesar':'<built in>',
                            'shuffle':'<built in>'},
                 'transposition':{'onecycle':'<built in>',
                                  'railfence':'<built in>',
                                  'reverse':'<built in>'}
                 }
    prof_delete('test')
    return(prof_list()==prof_test)

prof_tests = [prof_test_01, prof_test_02, prof_test_03, prof_test_04]

def verify_prof_tests():
    pass_number = 0
    total_number = len(prof_tests)
    for tc in prof_tests:
        if tc(): pass_number += 1
        else: print(f'Error: {tc.__name__}')
    print(f'Pass rate: {pass_number / total_number * 100}% ({pass_number} out of {total_number})')

verify_prof_tests()
