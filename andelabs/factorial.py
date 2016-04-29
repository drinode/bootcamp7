def factorial(number):
	'''
	Takes a number then returns the 
	factorial of the number
	'''
	if number == 0:
		return 1
	else :
		return number * factorial(number - 1)

print (factorial(4))
