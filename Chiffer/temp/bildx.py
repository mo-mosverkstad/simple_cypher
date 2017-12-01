for y in range(0, 6, 1):
	for x in range(0, 6, 1):
		if x+y==5 or x==y:
			print '*',
		else:
			print ' ',
	print