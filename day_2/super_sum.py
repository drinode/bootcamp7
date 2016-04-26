def super_sum(A):
	''' 
	Takes a list A, and :
	     -halves every even number
	     -doubles every odd  number
	And returns the sum of all

	'''
	total = 0
	for i in A:
		if i(A) % 2 == 0:
			total += (i / 2)
		else 
		    total =+ (i * 2)
	
	return total    	
