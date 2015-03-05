def sequence(n):
	x, previous = 1, 0
	count = 0
	while count < (n+1):
		print (x)
		x, previous = x+previous, x
		count +=1
		
sequence(10)
