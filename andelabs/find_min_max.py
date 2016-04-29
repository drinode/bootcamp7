def find_max_min(A):
	'''
	Returns the max and min number and puts them in an array
	'''
	l = []
	max_, min_ = (A[0], A[0])
	
	for i in A:
		if i > max_:
			max_ = i
		
		if i < min_:
			min_ = i
	
	l.append(min_)
	l.append(max_)
	if max_ == min_:
		return A
	return l

print (find_max_min)