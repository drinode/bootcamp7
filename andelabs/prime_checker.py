class PrimeChecker(object):
	'''
	Class that takes in a string arguement .
	When the instance of the class is called with .is_prime()
	should return true if number is a prime number 
	and false if it isn't
	'''
	def __init__(self, number=None):
		self.number = number
		if self.number == (''):
			return False 
		
	def is_prime(self):
		
		for i in range(2, n):
			if n % i == 0:
				return False
		return True

n = PrimeChecker(3)
print (n.is_prime())
		

