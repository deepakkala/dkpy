import math
print 'please enter the decimal digit till which we have to calculate pi'

def precision():
	x=int(raw_input())
	while x>50:	
		print 'print a lower digit'
		x=int(raw_input())
	else:
		print '%.*f' % (x, math.pi)
		
precision()
