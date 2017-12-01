continueFlag = True
exitList = ['exit', 'quit', 'bye', 'i will leave here', 'close', 'power off']

while continueFlag:
	msg = str(raw_input('echo>'))
	if msg.lower() in exitList:
		continueFlag = False
	else:
		print 'echo: ' + msg