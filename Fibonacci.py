def sequence(n):
	x, previous = 1, 0
	count = 0
	while count < (n+1):
		print (x)
		x, previous = x+previous, x
		count +=1
		
				
sequence(10)

"""def fibSequence(n):
	a, b = 0, 1
	for i in range(1, n+1):
		print a
		a, b = b, a+b
	return
	
fibSequence(2000)"""
		
		
"""
def sequence(n):
	x = 1
	previousa = 0
	previousx = 0
	count = 0
	while count < (n+1):
		print (x)
		previousx = x
		x += previousa
		previousa = previousx
		count +=1
		
				
sequence(10)"""