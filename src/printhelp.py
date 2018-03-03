from sys import stdout
import os

def printhelp(status, algorithm, key):
    f = open('help.scc', 'r')
    reading = f.readlines()
    f.close()
    counter = 0
    for i in reading:
        counter += 1
        print(i.strip())
        if counter > 27:
            input('--Press return for more--')
            os.system('CLS')
            counter = 0
    return status, algorithm, key
