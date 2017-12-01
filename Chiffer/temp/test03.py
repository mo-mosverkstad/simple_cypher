for y in range(0, 6, 1):
	print 'row ' + str(y) + ': ',
	for x in range(0, 6, 1):
		print '(' + str(y) + ', ' + str(x) + ')\t',
	print

for y in range(0, 6, 1):
	for x in range(0, 6, 1):
		if y == x:
			print '*', 
		else:
			print ' ',
	print