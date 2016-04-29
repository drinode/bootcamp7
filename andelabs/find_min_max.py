def find_max_min(A):
	'''
	Returns the max and min number and puts them in an array
	'''
	max_ , min_ = A[0], A[0]
	A = []
	B = A
	for i in A:
		if i > max_:
			max_ = 1
		if i < min_:
			min_ = 1
		if min_ == max_:
			return A.append(B)