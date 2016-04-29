 
def arith_geom(*A):
	'''
	Checks if the array passed is arithmetic or geometric
		-neither arith,geo in progression 
		or if array is empty
	'''
	count = 0
	for i in A:
		if len(i) == 0:
			return 0
		for x in range(len(i)-1):
			d = i[x]
			d1 = i[x+1]
			d2 = i[x+2]
		
			if (d1-d) == (d2-d1):
				return 'Arithmetic'
			elif(d1/d)==(d2/d1):
				return 'Geometric'
			elif A == None:
				return 0
			else:
				return -1
		
			
print (arith_geom([2, 6, 18, 54, 162]))
print (arith_geom([]))
print (arith_geom([5, 11, 17, 23, 29, 35, 41]))