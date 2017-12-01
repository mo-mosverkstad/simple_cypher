from caesarLib import caeCypher
from reversedLib import reverseCypher
from simpleMappingLib import simpleMapping
from mappingLib import mappingCypher

PROMPT = 'Mos Cypher:)'
continueFlag = True

while continueFlag:
	opt = str(raw_input(PROMPT + ' Please input option (BYE, CAE, REV, SMP, MAP)?'))
	if opt =='BYE':
		continueFlag = False
	elif opt =='CAE':
		caeCypher()
	elif opt =='REV':
		reverseCypher()
	elif opt =='SMP':
		simpleMapping()
	elif opt =='MAP':
		mappingCypher()