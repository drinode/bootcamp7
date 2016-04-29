def fizz_buzz(i):
	'''
	A function fizz_buzz takes in a number,checks 
		-if  divisible by 3 and 5returns "fizz_buzz"
		-if  divisible by 5 return "Buzz"
		-if  divisible by 3 returns "Fizz"
		-if  divisible by neither return itself.
	'''
	if  i % 3 == 0 and i % 5 == 0 :
		return "FizzBuzz"
	elif i % 3 == 0:
		return "Fizz"
	elif i % 5 == 0:
		return "Buzz"
	else:
		return i

print (fizz_buzz(3))
print (fizz_buzz(5))
print (fizz_buzz(75))
print (fizz_buzz(43))