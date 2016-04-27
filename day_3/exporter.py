#global var is not a good practice 
people = [('Joe',45),
		  ('Janet',89),
		  ('Jee',99)]


def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {} , and I'm {} years old".format(name,age)
def max_min(A):
	'''
	Returns the max value - min value.
	'''
	#return max(A) - min(A)
	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = 1
		if i < min_:
			min_ = 1

			return max_ - min_
