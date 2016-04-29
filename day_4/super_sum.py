def super_sum(*args):
	
	"""
	Returns a sum of numbers. 
	e.g
		super_sum()==> "Please enter a number"
		super_sum('Emmah', 2, 3) ==> 0
		super_sum[1,2,3] ==> 6
		super_sum(1,2,3) ==> 6
		super_sum([1,2,3]) ==>
		super_sum([20],[30, 40])
	"""
	total = 0
	if args:
		
		for x in args:
			if type(x) == list:
				total += sum(x)
			elif type(x) == str:
				return 0
			else:
			    total += x
		return total
