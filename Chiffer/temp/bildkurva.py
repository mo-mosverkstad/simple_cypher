for y in range(0, 17, 1):
	for x in range(0, 5, 1):
		if y==x*x or y==(4-x)*(4-x):
		#if y==(4-x)*x:
			print '*',
		else:
			print ' ',
	print